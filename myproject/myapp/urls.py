from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('electronic', views.electronic, name='electronic'),
    path('fashion', views.fashion, name='fashion'),
    path('jewellery', views.jewellery, name='jewellery'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('secces/', views.secces, name='secces'),
    path('log_out/', views.logout_view, name='log_out'),
    path('korzina/', views.korzina, name='korzina'),
    path('cart/', views.cart_detail, name='cart_detail'),
    
    # Обновленный путь для добавления товара в корзину
    path('cart/add/<str:model_name>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
