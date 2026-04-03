import logging
from decimal import Decimal

from django.utils import timezone
from django.db import transaction
from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from core.models import Order, DailyRevenue

logger = logging.getLogger(__name__)


def update_daily_revenue():
    """
    Tính toán doanh thu và số lượng đơn hàng trong ngày hiện tại
    theo múi giờ cấu hình, rồi upsert vào bảng DailyRevenue.
    """
    now = timezone.localtime()
    today = now.date()

    logger.info(f"Đang tính ETL doanh thu cho ngày {today}...")

    with transaction.atomic():
        orders_today = Order.objects.filter(created_at__date=today)
        total_orders = orders_today.count()

        revenue_expr = ExpressionWrapper(
            F("orderitem__quantity") * F("orderitem__price_at_order"),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        )

        revenue_calc = orders_today.aggregate(
            total_revenue=Sum(revenue_expr)
        )

        total_revenue = revenue_calc["total_revenue"] or Decimal("0.00")

        revenue_record, created = DailyRevenue.objects.update_or_create(
            date=today,
            defaults={
                "total_orders": total_orders,
                "total_revenue": total_revenue,
            }
        )

    action = "Đã tạo mới" if created else "Đã cập nhật"
    logger.info(
        f"{action} doanh thu ngày {today}: {total_orders} đơn hàng, doanh thu {total_revenue}"
    )

    return revenue_record