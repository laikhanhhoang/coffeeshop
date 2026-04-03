# Yêu cầu: Viết Views và URLs cho hệ thống quản lý
Hãy giúp tôi tạo các hàm xử lý logic (Views) trong `core/views.py` và cấu hình file `core/urls.py`.

## 1. Cấu hình URLs
- `/` : Trang Thêm đơn hàng (Root link). Name: `add_order`.
- `/doanh-thu-hom-nay/` : Trang Xem doanh thu hôm nay. Name: `today_revenue`.
- `/tong-hop-thong-tin/` : Trang Tổng hợp thông tin (Dashboard). Name: `dashboard`.

## 2. Logic của Views
1. **add_order (Thêm đơn hàng):**
   - Query danh sách các đơn hàng đã được tạo trong **ngày hôm nay** (dựa theo múi giờ GMT+7) để truyền ra context.
   - Trả về template `add_order.html`.

2. **today_revenue (Xem doanh thu hôm nay):**
   - Query lấy bản ghi `DailyRevenue` của ngày hôm nay.
   - Trả về thông tin: ngày, số lượng đơn, tổng doanh thu ra context.
   - Trả về template `today_revenue.html`.

3. **dashboard (Tổng hợp thông tin):**
   - Trả về dữ liệu cần thiết để vẽ biểu đồ cho tuần và tháng.
   - Query 1: Danh sách tổng doanh thu và số đơn hàng theo từng ngày trong tuần hiện tại (từ Thứ Hai đến hiện tại).
   - Query 2: Danh sách tổng doanh thu và số đơn hàng theo từng ngày trong tháng hiện tại.
   - (Gợi ý: Dùng `TruncDate` và `Count`, `Sum` của Django ORM để group by ngày, sau đó truyền ra context dưới dạng JSON để Frontend dùng Chart.js vẽ).
   - Trả về template `dashboard.html`.