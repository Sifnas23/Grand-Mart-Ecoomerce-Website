from django.shortcuts import render, redirect
from MyApp.models import Category_db, Product_db
from WebApp.models import SignUpdb, Contactdb, Cartdb,  Customerdb
from django.db.models import Sum

def homepage(request):
    data = Category_db.objects.all()
    return render(request, "Homepage.html", {'data':data})
def aboutus(request):
    data = Category_db.objects.all()
    return render(request, "AboutUs.html", {'data':data})
def contactus(request):
    data = Category_db.objects.all()
    return render(request, "ContactUs.html", {'data':data})
def category(request, itemcatg):
    product = Product_db.objects.filter(Category=itemcatg)
    data = Category_db.objects.all()
    data1 = Product_db.objects.all()
    return render(request, "Category.html", {'data': data, 'product': product, 'data1': data1})
def singlepro(request,dataid):
    data = Category_db.objects.all()
    product = Product_db.objects.get(id=dataid)
    return render(request, "Singleproduct.html", {'data': data, 'product': product})
def userlogin(request):
    return render(request,"userlogin.html")

def  signupdbsave(request):
    if request.method == "POST":
        em = request.POST.get("email")
        na = request.POST.get("name")
        pa = request.POST.get("password")
        co = request.POST.get("confirm")
        obj = SignUpdb(Email=em, Username=na, Password=pa, Confirm=co)
        obj.save()
        return redirect(userlogin)

def userlogindata(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if SignUpdb.objects.filter(Username=username_r, Password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r
            return redirect(homepage)
        else:
            return redirect(userlogin)
    return redirect(userlogin)

def contactdbsave(request):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        su = request.POST.get("subject")
        me = request.POST.get("message")
        obj = Contactdb(Name=na, Email=em, Subject=su, Message=me)
        obj.save()
        return redirect(contactus)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homepage)

def cartfun(request):
    data1 = Category_db.objects.all()
    data = Cartdb.objects.all()
    grandtotal = data.aggregate(Sum("Total_Price"))["Total_Price__sum"]
    return render(request, "Cart.html", {"data": data, "grandtotal": grandtotal, 'data1': data1})

def Cartdbsave(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('productprice')
        quan = request.POST.get('qty')
        total = request.POST.get('totalprice')
        # img = request.FILES['image']
        obj = Cartdb(Name=name, Price=price, Quantity=quan, Total_Price=total)
        obj.save()
        return redirect(cartfun)

def cart_product_del(request, dataid):
    data = Cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartfun)


def customerdbsave(request):
    if request.method == "POST":
        na = request.POST.get("name")
        add = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        code = request.POST.get("code")
        num = request.POST.get("number")
        em = request.POST.get("email")
        obj = Customerdb(Name=na, Address=add, City=city, State=state,  Postalcode=code, PhoneNumber=num, EmailId=em)
        obj.save()
        return redirect(cartfun)

def check_out_fun(request):
    data = Cartdb.objects.all()
    data.delete()
    return render(request, "check_out.html")

