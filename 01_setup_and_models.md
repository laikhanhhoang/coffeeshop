# Yêu cầu: Khởi tạo Project Django & Models
Bạn là một lập trình viên Python/Django Senior. Hãy giúp tôi viết code để thiết lập một project Django quản lý bán cà phê.

## 1. Cấu hình Project & Database (Quan trọng)
- Tên project: `coffee_shop`. Tên app: `core`.
- **Database: Sử dụng PostgreSQL với thông tin sau:**
    - Engine: `django.db.backends.postgresql`
    - NAME: `CoffeeShop`
    - USER: `app_user`
    - PASSWORD: `userpassword`
    - HOST: `localhost`
    - PORT: `5432`

- **Múi giờ:** Thiết lập ứng dụng chạy theo giờ Việt Nam (GMT+7). 
    - Cấu hình `TIME_ZONE = 'Asia/Ho_Chi_Minh'` và `USE_TZ = True` trong `settings.py`.

## 2. Thiết kế Database (Models)
Hãy tạo code trong file `core/models.py` với các models sau:

1. **Product (Sản phẩm)**
   - `name`: CharField (tên sản phẩm).
   - `price`: DecimalField (giá sản phẩm).

2. **Order (Đơn hàng)**
   - `created_at`: DateTimeField (tự động lưu thời gian tạo theo GMT+7).
   - Quan hệ Many-to-Many với `Product` thông qua bảng trung gian `OrderItem`.

3. **OrderItem (Chi tiết đơn hàng)**
   - Khóa ngoại tới `Order`.
   - Khóa ngoại tới `Product`.
   - `quantity`: IntegerField (số lượng).
   - `price_at_order`: DecimalField (lưu giá tại thời điểm bán).

4. **DailyRevenue (Doanh thu theo ngày)**
   - `date`: DateField (unique).
   - `total_orders`: IntegerField (mặc định 0).
   - `total_revenue`: DecimalField (mặc định 0).

Yêu cầu thêm: Viết code cho `admin.py` để quản lý các model này. Cung cấp lệnh pip install cần thiết (ví dụ: django, psycopg2-binary).