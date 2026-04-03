from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_order, name='add_order'),
    path('doanh-thu-hom-nay/', views.today_revenue, name='today_revenue'),
    path('tong-hop-thong-tin/', views.dashboard, name='dashboard'),
]
