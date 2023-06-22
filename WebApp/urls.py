from django.urls import path
from WebApp import views

urlpatterns=[
    path('', views.homepage, name="homepage"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('category/<itemcatg>/', views.category, name="category"),
    path('singlepro/<int:dataid>', views.singlepro, name="singlepro"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('signupdbsave/', views.signupdbsave, name="signupdbsave"),
    path('userlogindata/', views.userlogindata, name="userlogindata"),
    path('contactdbsave/', views.contactdbsave, name="contactdbsave"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cartfun/', views.cartfun, name="cartfun"),
    path('Cartdbsave/', views.Cartdbsave, name="Cartdbsave"),
    path('cart_product_del/<int:dataid>', views.cart_product_del, name="cart_product_del"),
    path('customerdbsave/', views.customerdbsave, name="customerdbsave"),
    path('check_out_fun/', views.check_out_fun, name="check_out_fun")

]