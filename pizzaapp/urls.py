from django.urls import path

from pizzaapp.views import add_pizza_view, admin_home_view, admin_login_view, admin_logout_view, authenticate_admin_view, authenticate_customer_view, customer_create_view, customer_home_view, customer_login_view, customer_logout_view, customer_order_view, customer_register_view, delete_pizza_view, customer_orders_view, admin_orders_view,admin_accept_order_view, admin_decline_order_view


urlpatterns = [
    path('admin/',admin_login_view,name='admin-login'),
    path('admin/authenticate/',authenticate_admin_view,name='admin-authenticate'),
    path('admin/logout/',admin_logout_view,name='admin-logout'),
    path('admin/home/',admin_home_view,name='admin-home'),
    path('admin/add-pizza/',add_pizza_view,name='admin-add-pizza'),
    path('admin/delete-pizza/<int:id>/',delete_pizza_view,name='admin-delete-pizza'),
    path('admin/orders/',admin_orders_view,name='admin-orders'),
    path('admin/order/<int:id>/accept/',admin_accept_order_view,name='admin-order-accept'),
    path('admin/order/<int:id>/decline/',admin_decline_order_view,name='admin-order-decline'),
    

    path('',customer_login_view,name='customer-login'),
    path('customer/register/',
    customer_register_view,name='customer-register'),
    path('customer/authenticate/',authenticate_customer_view,name='customer-authenticate'),
    path('customer/create/',
    customer_create_view,name='customer-create'),
    path('customer/logout/',customer_logout_view,name='customer-logout'),
    path('customer/home/',
    customer_home_view,name='customer-home'), 
    path('customer/order/',
    customer_order_view,name='customer-order'),   
    path('customer/orders/',
    customer_orders_view,name='customer-orders'),   
]
