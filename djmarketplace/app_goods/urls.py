from django.urls import path
from app_goods.views import GoodListView, GoodDetailView, BasketView, ReportView

urlpatterns = [
    path('goodlist/', GoodListView.as_view(), name='goodlist'),
    path('good_detail/<int:pk>', GoodDetailView.as_view(), name='gooddetail'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('report/', ReportView.as_view(), name='rep'),
]