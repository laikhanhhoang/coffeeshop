# Yêu cầu: Viết Frontend Templates (HTML/CSS/JS)
Sử dụng Bootstrap 5 (hoặc Tailwind CSS) qua CDN để làm giao diện nhanh chóng. Hãy tạo cấu trúc template kế thừa (extends) trong thư mục `templates/`.

## 1. Base Template (`base.html`)
- Chứa Layout chung chia màn hình làm 2 phần:
  - **Cột bên trái (Sidebar):** Rộng khoảng 20-25%.
  - **Cột bên phải (Main Content):** Rộng phần còn lại.
- **Sidebar có 3 menu item:**
  1. Thêm đơn hàng (link tới url `add_order`)
  2. Xem doanh thu hôm nay (link tới url `today_revenue`)
  3. Tổng hợp thông tin (link tới url `dashboard`)
- **Logic UI Sidebar:** Dựa vào url hiện tại (dùng `request.resolver_match.url_name`), CSS của menu item sẽ thay đổi:
  - Trang đang active: Chữ in đậm (font-weight: bold), màu nổi bật.
  - Các trang không active: Chữ in mờ (opacity: 0.6, màu nhạt hơn).

## 2. Các trang con (Kế thừa base.html)

1. **`add_order.html`:**
   - Cột phải hiển thị danh sách các đơn hàng hôm nay (bảng hoặc thẻ card).
   - Có một nút `+ Thêm đơn hàng mới` (nút này hiện form hoặc modal để chọn Product, nhập số lượng và submit POST request).

2. **`today_revenue.html`:**
   - Cột phải có một khung (Card/Box) to, hiển thị 3 dòng thông tin:
     - Ngày: [Ngày hôm nay]
     - Tổng số đơn hàng: [Số lượng]
     - Tổng doanh thu: [Số tiền] VNĐ.

3. **`dashboard.html`:**
   - Cột phải chứa các biểu đồ. Nhúng CDN của thư viện `Chart.js`.
   - Tạo ít nhất 2 biểu đồ dạng cột (Bar chart) hoặc đường (Line chart):
     - Biểu đồ 1: So sánh doanh thu và số đơn hàng các ngày trong tuần (tính từ Thứ 2).
     - Biểu đồ 2: So sánh doanh thu và số đơn hàng trong tháng.
   - Render dữ liệu dạng JSON từ View vào script để vẽ biểu đồ.