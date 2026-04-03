import random
from decimal import Decimal
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction

from core.models import Product, Order, OrderItem


class Command(BaseCommand):
    help = "Tạo 20 đơn hàng random để test ETL doanh thu"

    def handle(self, *args, **options):
        products = list(Product.objects.all())

        if not products:
            self.stdout.write(self.style.ERROR("Không có Product nào trong DB. Hãy tạo sản phẩm trước."))
            return

        created_orders = 0

        with transaction.atomic():
            range_of_orders = random.randint(1,3)
            for i in range(range_of_orders):
                # Tạo order mới
                order = Order.objects.create()

                # Random 1 đến 4 sản phẩm trong 1 đơn
                selected_products = random.sample(
                    products,
                    k=min(random.randint(1, 4), len(products))
                )

                for product in selected_products:
                    quantity = random.randint(1, 5)

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price_at_order=product.price
                    )

                # Optional: random created_at trong hôm nay để test ETL
                now = timezone.localtime()
                seconds_later = 30*i
                fake_created_at = now + timedelta(seconds=seconds_later)

                Order.objects.filter(id=order.id).update(created_at=fake_created_at)

                created_orders += 1

        self.stdout.write(self.style.SUCCESS(f"Đã tạo thành công {created_orders} đơn hàng random."))