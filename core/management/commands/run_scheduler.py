import logging

from django.core.management.base import BaseCommand
from django.db import close_old_connections
from django.utils import timezone

from core.tasks import update_daily_revenue

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Chạy ETL cập nhật doanh thu 1 lần rồi thoát."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Bắt đầu chạy job update_daily_revenue..."))

        try:
            close_old_connections()

            start_time = timezone.localtime()
            self.stdout.write(f"Start time: {start_time}")

            update_daily_revenue()
            self.stdout.write(self.style.SUCCESS("Đã chạy xong update_daily_revenue."))

            end_time = timezone.localtime()
            self.stdout.write(self.style.SUCCESS(f"End time: {end_time}"))
            self.stdout.write(self.style.SUCCESS("Job hoàn tất. Chương trình sẽ thoát."))

        except Exception as e:
            logger.exception("Lỗi khi chạy run_scheduler")
            self.stderr.write(self.style.ERROR(f"Lỗi khi chạy job: {e}"))
            raise

        finally:
            close_old_connections()