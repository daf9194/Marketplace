from django.urls import path
from app_users.views import edit_bal_view, register_view, accuont_view, MyLoginView, MyLogoutView

urlpatterns = [
    path('register/', register_view, name='reg'),
    path('account/', accuont_view, name='acc'),
    path('login/', MyLoginView.as_view() , name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('edit_balance/', edit_bal_view, name='add_mony'),

]