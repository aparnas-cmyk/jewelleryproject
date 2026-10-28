from django.urls import path
from jewelapp import views
from webapp import views
urlpatterns = [
path('homepage/',views.homepage,name='homepage'),
path('contact/',views.contact,name='contact'),
path('contact_save/',views.contact_save,name='contact_save'),
path('filterproject/<orn_name>/',views.filterproject,name='filterproject'),
path('singleproducts/<orn_id>/',views.singleproducts,name='singleproducts'),
path('userregister/',views.userregister,name='userregister'),
path('save_register/',views.save_register,name='save_register'),
path('',views.loginform,name='loginform'),
path('userlogin/',views.userlogin,name='userlogin'),
path('about/',views.about,name='about'),
path('cart/',views.cart,name='cart'),
path('savecart/',views.savecart,name='savecart'),
path('deletecart/<cart_id>/',views.deletecart,name='deletecart'),
path('checkout/',views.checkout,name='checkout'),
path('save_checkout/',views.save_checkout,name='save_checkout'),
path('payment/',views.payment,name='payment')
]