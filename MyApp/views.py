from django.shortcuts import render, redirect
from MyApp.models import Category_db,Product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import Contactdb, Cartdb, Customerdb
from django.contrib import messages




def indexfun(request):
    return render(request, "index.html")

def addcategory(request):
    return render(request,"AddCategory.html")

def categorydbfun(request):
    if request.method == "POST":
        na = request.POST.get('name')
        im = request.FILES['image']
        de = request.POST.get('description')
        obj = Category_db(Name=na, Image=im, Description=de)
        obj.save()
        messages.success(request, "Category saved successfully")
        return redirect(addcategory)

def dispalaycategorydata(request):
    data = Category_db.objects.all()
    return render(request, "display_category.html", {'data' : data})

def editcategorydata(request, dataid):
    data = Category_db.objects.get(id=dataid)
    print(data)
    return render(request, "editcategorydata.html", {'data': data})

def updatecategory(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('description')
        try:
            im = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Category_db.objects.get(id=dataid).Image
        Category_db.objects.filter(id=dataid).update(Name=na, Image=file, Description=de)
        return redirect(dispalaycategorydata)

def delcategory(request, dataid):
    data = Category_db.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted Successfully")
    return redirect(dispalaycategorydata)

def addproductfun(request):
    data = Category_db.objects.all()
    return render(request, "AddProduct.html", {"data":data})

def productdbfun(request):
    if request.method == "POST":
        cat = request.POST.get('category')
        pro = request.POST.get('product')
        pri = request.POST.get('price')
        qua = request.POST.get('quantity')
        des = request.POST.get('description')
        img = request.FILES['image']
        obj = Product_db(Category=cat, Product=pro, Price=pri, Quantity=qua, Description=des, Image=img)
        obj.save()
        messages.success(request, "Product saved successfully")
        return redirect(addproductfun)

def displayproductfun(request):
    data = Product_db.objects.all()
    return render(request,"displayproducts.html",{"data":data})

def editproductfun(request,dataid):
    data = Product_db.objects.get(id=dataid)
    da = Category_db.objects.all()
    print(data)
    return render(request,"editproductdata.html",{"data":data,"da":da})

def updateproduct(request,dataid):
    if request.method == "POST":
        cat = request.POST.get('category')
        pro = request.POST.get('product')
        pri = request.POST.get('price')
        qua = request.POST.get('quantity')
        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Product_db.objects.get(id=dataid).Image
        Product_db.objects.filter(id=dataid).update(Category=cat, Product=pro, Price=pri, Quantity=qua, Description=des, Image=file)
        return redirect(displayproductfun)

def defproduct(request,dataid):
    data = Product_db.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproductfun)

def loginfun(request):
    return render(request, "Admin_login.html")

def adminloginfun(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(indexfun)
            else:
                return redirect(loginfun)
        else:
            return redirect(loginfun)

def adminlogoutfun(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginfun)

def displaycontactfun(request):
    data = Contactdb.objects.all()
    return render(request, "displaycoontactdetails.html", {"data":data})

def contactdelfun(request,dataid):
    data = Contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontactfun)

def displaycarttfun(request):
    data = Cartdb.objects.all()
    return render(request, "displaycartdata.html", {"data":data})

def cartdelfun(request,dataid):
    data = Cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycarttfun)

def displaycustomerfun(request):
    data = Customerdb.objects.all()
    return render(request, "displaycustomerdata.html", {"data": data})

def customerdbfun(request,dataid):
    data = Customerdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycustomerfun)



