from django.urls import path
from .views import UserCreateView, UserListView, ProductCreateView, ProductListView, ProductWithImagesCreateView, SendOTPView, UserLoginView, UserCartProductCreateView

app_name = 'accounts'

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/create-with-images/', ProductWithImagesCreateView.as_view(), name='product_create_with_images'),
    path('send-otp/', SendOTPView.as_view(), name='send_otp'),
    path('user-login/', UserLoginView.as_view(), name='user_login'),
    path('user-cart-products/create/', UserCartProductCreateView.as_view(), name='user_cart_product_create'),
]