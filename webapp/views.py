from django.shortcuts import render,redirect
from jewelapp.models import Jewelcate_Db,Ornaments_Db
from webapp.models import contact_Db,Register_db,cart_db,Order_db

def homepage(request):
    data=Jewelcate_Db.objects.all()
    return render(request,'home.html',{'data':data})
def contact(request):
    return render(request,'contact.html')
def contact_save(request):
    if request.method =="POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Subject= request.POST.get('Subject')
        Message = request.POST.get('Message')
        obj=contact_Db(Name=Name,Email=Email,Subject=Subject,Message=Message)
        obj.save()
        return redirect('contact')
def filterproject(request,orn_name):
    products=Ornaments_Db.objects.filter(Category_Name=orn_name)
    return render(request,'filterproducts.html',{'products':products})
def singleproducts(request,orn_id):
    data = Ornaments_Db.objects.get(id=orn_id)
    return render(request,'singleproduct.html',{'data':data})
def userregister(request):
    return render(request,'userregister.html')
def save_register(request):
    if request.method =="POST":
        Full_Name = request.POST.get('Full_Name')
        password= request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        Email = request.POST.get('Email')
        number = request.POST.get('number')
        obj = Register_db(Full_Name=Full_Name, password=password, confirm_password=confirm_password, Email=Email,number=number)
        obj.save()
        return redirect('userregister')

def loginform(request):
    return render(request,'loginform.html')
def userlogin(request):
    if request.method =="POST":
        un=request.POST.get('username')
        pw=request.POST.get('password')
        if Register_db.objects.filter(Full_Name=un,password=pw).exists():
            request.session['Full_Name']=un
            request.session['password']=pw
            return redirect(homepage)
        else:
            return redirect(loginform)
    else:
        return render(loginform)

def about(request):
    return render(request,'about.html')
def cart(request):
    subtotal=0
    total=0
    data=cart_db.objects.filter(Name=request.session['Full_Name'])
    for i in data:
        subtotal+=i.total_price

        if subtotal>150000:
            delivery_charge=1000
        else:
            delivery_charge=5000
        total = subtotal + delivery_charge
    return render(request,'cart.html',{'data':data,'subtotal':subtotal,'total':total,'delivery_charge':delivery_charge})

def savecart(request):
    if request.method =="POST":
        quantity=request.POST.get('quantity')
        proname=request.POST.get('productname')
        username=request.POST.get('name')
        price=request.POST.get('price')
        total=request.POST.get('total')

    try:
        x=Ornaments_Db.objects.get(Product_Name=proname)
        img=x.Ornaments_img
    except Ornaments_Db.DoesNotExist:
        img=none
    obj= cart_db(quantity=quantity,product_name=proname,Name=username,price=price,total_price=total,product_image=img)
    obj.save()
    return redirect('cart')
def deletecart(request,cart_id):
    x=cart_db.objects.filter(id=cart_id)
    x.delete()
    return redirect('cart')
def checkout(request):
    subtotal = 0
    total = 0
    data = cart_db.objects.filter(Name=request.session['Full_Name'])
    for i in data:
        subtotal += i.total_price

        if subtotal > 150000:
            delivery_charge = 1000
        else:
            delivery_charge = 5000
        total = subtotal+delivery_charge
    return render(request,'checkout.html',{'data':data,'subtotal':subtotal,'total':total,'delivery_charge':delivery_charge})


def save_checkout(request):
    if request.method =="POST":
        first_Name = request.POST.get('fname')
        last_Name = request.POST.get('lname')
        email= request.POST.get('email')
        number = request.POST.get('mobile')
        address = request.POST.get('address')
        country = request.POST.get('country')
        price = request.POST.get('price')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        obj = Order_db(first_Name=first_Name,last_Name=last_Name,email=email,mobile=number,address=address,country=country,total_price=price,city=city,state=state,zip_code=zip_code)
        obj.save()
        return redirect(payment)

def payment(request):
    subtotal = 0
    total = 0
    data = cart_db.objects.filter(Name=request.session['Full_Name'])
    for i in data:
        subtotal += i.total_price

        if subtotal > 150000:
            delivery_charge = 1000
        else:
            delivery_charge = 5000
        total = subtotal+delivery_charge
    return render(request,'payment.html',{'data':data,'subtotal':subtotal,'total':total,'delivery_charge':delivery_charge})

# Create your views here.
