from django.urls import path
from MyApp import views

urlpatterns = [
    path('indexfun/', views.indexfun, name="indexfun"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('categorydbfun/', views.categorydbfun, name="categorydbfun"),
    path('dispalaycategorydata/', views.dispalaycategorydata, name="dispalaycategorydata"),
    path('editcategorydata/<int:dataid>', views.editcategorydata, name="editcategorydata"),
    path('updatecategory/<int:dataid>', views.updatecategory, name="updatecategory"),
    path('delcategory/<int:dataid>', views.delcategory, name="delcategory"),
    path('addproductfun/', views.addproductfun, name="addproductfun"),
    path('productdbfun/', views.productdbfun,name="productdbfun"),
    path('displayproductfun/',views.displayproductfun, name="displayproductfun"),
    path('editproductfun/<int:dataid>', views.editproductfun, name="editproductfun"),
    path('updateproduct/<int:dataid>', views.updateproduct, name="updateproduct"),
    path('defproduct/<int:dataid>', views.defproduct, name="defproduct"),
    path('loginfun/', views.loginfun, name="loginfun"),
    path('adminloginfun/',views.adminloginfun,name="adminloginfun"),
    path('adminlogoutfun/', views.adminlogoutfun, name="adminlogoutfun"),
    path('displaycontactfun/', views.displaycontactfun, name="displaycontactfun"),
    path('contactdelfun/<int:dataid>', views.contactdelfun, name="contactdelfun"),
    path('displaycarttfun/', views.displaycarttfun, name="displaycarttfun"),
    path('displaycustomerfun/', views.displaycustomerfun, name="displaycustomerfun"),
    path('customerdbfun/<int:dataid>', views.customerdbfun, name="customerdbfun")
]