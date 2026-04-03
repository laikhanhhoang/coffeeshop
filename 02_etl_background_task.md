# Yêu cầu: Viết ETL Job cập nhật doanh thu tự động
Dựa trên các models ở app `core` đã tạo, hãy giúp tôi viết một tiến trình chạy ngầm (background task) để tính toán doanh thu.

## 1. Logic ETL
- Viết một hàm Python (ví dụ: `update_daily_revenue()`) thực hiện các việc sau:
  - Lấy ngày hiện tại theo múi giờ GMT+7 (Asia/Ho_Chi_Minh).
  - Query tất cả các `Order` được tạo trong ngày hôm nay.
  - Đếm tổng số đơn hàng.
  - Tính tổng doanh thu của các đơn hàng đó.
  - Cập nhật hoặc tạo mới (update_or_create) bản ghi trong bảng `DailyRevenue` với ngày hôm nay.

## 2. Lập lịch (Scheduling)
- Task này cần được chạy tự động **mỗi 5 phút**.
- Hãy hướng dẫn và cung cấp code sử dụng `APScheduler` (thông qua package `django-apscheduler`) vì nó nhẹ và dễ tích hợp cho ETL đơn giản, hoặc viết dưới dạng Custom Management Command (`python manage.py run_etl`) kết hợp thư viện `schedule`.