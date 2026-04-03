#!/bin/bash

# Cách lấy đường dẫn thư mục hiện tại an toàn nhất
BASE_DIR=$(pwd)
# Hoặc chuẩn hơn nếu script được gọi từ nơi khác:
# BASE_DIR=$(cd "$(dirname "$0")" && pwd)

PYTHON_BIN="$BASE_DIR/antenv/bin/python"
MANAGE_PY="$BASE_DIR/manage.py"

echo "Running from: $BASE_DIR"

# Chạy Task 1 phút
while true; do
  $PYTHON_BIN $MANAGE_PY run_scheduler
  sleep 60
done &

# Chạy Task 3 phút
while true; do
  $PYTHON_BIN $MANAGE_PY seed_orders
  sleep 180
done &

# Chạy Web chính
$PYTHON_BIN -m gunicorn --bind=0.0.0.0 --timeout 600 coffee_shop.wsgi