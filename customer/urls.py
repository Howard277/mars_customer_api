from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health),
    # 配置“客户”模块接口地址
    path('get_customer_info', views.get_customer_info),
]
