from django.contrib import admin
from django.urls import path
from marts import views
urlpatterns = [
    path('',views.signin,name='signin'),
    path('signin/',views.signin,name='signin'),
    path('home/',views.home,name='home'),
    path('category/',views.category,name='category'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dairy/',views.dairy,name='dairy'),
    path('cooking/',views.cooking,name='cooking'),
    path('fruit/',views.fruit,name='fruit'),
    path('packaged/',views.packaged,name='packaged'),
    path('user/',views.user,name='user'),
    path('cart/',views.cart,name='cart'),
    path('signout/',views.signout,name='signout'),
    path('detail',views.detail,name="detail"),
    path('cart_page',views.cart_page,name="cart_page"),
    path('get-cart-products/',views.get_cart_products,name="get_cart_products"),
    path('get-wishlist-products/',views.get_wishlist_products,name="get_wishlist_products"),
    path('wishlist',views.wishlist,name='wishlist'),
    path('create-order/',views.create_order,name="create_order")
]