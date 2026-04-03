import json
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Order, DailyRevenue, Product, OrderItem
from django.db import transaction
from django.contrib import messages

def add_order(request):
    """
    Trang thêm hóa đơn (trang chủ)
    Hiển thị danh sách đơn hàng trong ngày hôm nay.
    """
    if request.method == 'POST':
        product_ids = request.POST.getlist('product_id[]')
        quantities = request.POST.getlist('quantity[]')

        # Lọc dữ liệu hợp lệ
        items = []
        for product_id, quantity in zip(product_ids, quantities):
            if product_id and quantity:
                try:
                    quantity = int(quantity)
                    if quantity > 0:
                        items.append((int(product_id), quantity))
                except ValueError:
                    continue

        if items:
            with transaction.atomic():
                order = Order.objects.create()

                for product_id, quantity in items:
                    try:
                        product = Product.objects.get(id=product_id)
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            quantity=quantity,
                            price_at_order=product.price
                        )
                    except Product.DoesNotExist:
                        continue

            messages.success(request, f"Đã tạo đơn hàng #{order.id} thành công!")

        else:
            messages.error(request, "Đơn hàng không hợp lệ. Vui lòng chọn ít nhất 1 sản phẩm.")

        return redirect('add_order')

    now = timezone.localtime()
    today = now.date()

    start_of_day = timezone.make_aware(
        timezone.datetime.combine(today, timezone.datetime.min.time())
    )
    end_of_day = timezone.make_aware(
        timezone.datetime.combine(today, timezone.datetime.max.time())
    )

    orders_today = Order.objects.filter(
        created_at__range=(start_of_day, end_of_day)
    ).order_by('-created_at').prefetch_related('orderitem_set__product')

    products = Product.objects.all()

    context = {
        'orders_today': orders_today,
        'products': products,
    }
    return render(request, 'add_order.html', context)

def today_revenue(request):
    """
    Trang xem báo cáo doanh thu của hôm nay.
    """
    now = timezone.localtime()
    today = now.date()

    daily_record = DailyRevenue.objects.filter(date=today).first()
    
    context = {
        'date': today,
        'total_orders': daily_record.total_orders if daily_record else 0,
        'total_revenue': daily_record.total_revenue if daily_record else 0.00,
    }
    return render(request, 'today_revenue.html', context)

def dashboard(request):
    """
    Trang tổng hợp thông tin (Dashboard) theo tuần và tháng
    Thay vì đếm và truncate lại từ bảng Order, ta query trực tiếp từ DailyRevenue
    đã được ETL tự động tối ưu hóa để lấy danh sách doanh thu.
    """
    now = timezone.localtime()
    today = now.date()

    # == TÍNH DỮ LIỆU TUẦN ==
    # Từ Thứ Hai tuần này đến hiện tại
    start_of_week = today - timezone.timedelta(days=today.weekday())
    weekly_records = DailyRevenue.objects.filter(date__range=(start_of_week, today)).order_by('date')
    
    weekly_labels = [record.date.strftime("%d/%m") for record in weekly_records]
    weekly_orders = [record.total_orders for record in weekly_records]
    weekly_revenues = [float(record.total_revenue) for record in weekly_records]

    # == TÍNH DỮ LIỆU THÁNG ==
    start_of_month = today.replace(day=1)
    monthly_records = DailyRevenue.objects.filter(date__range=(start_of_month, today)).order_by('date')

    monthly_labels = [record.date.strftime("%d/%m") for record in monthly_records]
    monthly_orders = [record.total_orders for record in monthly_records]
    monthly_revenues = [float(record.total_revenue) for record in monthly_records]

    context = {
        'weekly_labels': json.dumps(weekly_labels),
        'weekly_orders': json.dumps(weekly_orders),
        'weekly_revenues': json.dumps(weekly_revenues),

        'monthly_labels': json.dumps(monthly_labels),
        'monthly_orders': json.dumps(monthly_orders),
        'monthly_revenues': json.dumps(monthly_revenues),
    }

    return render(request, 'dashboard.html', context)

