from django.urls import path
from pizzaapp.views import admin_login_view, admin_logout_view, authenticate_admin_view, admin_home_view
urlpatterns = [
    path('',admin_login_view,name='admin-login'),
    path('authenticate/',authenticate_admin_view,name='admin-authenticate'),
    path('logout/',admin_logout_view,name='admin-logout'),
    path('home/',admin_home_view,name='admin-home'),
    
]
