from django.shortcuts import render,redirect
from jewelapp.models import Jewelcate_Db,Ornaments_Db
from webapp.models import contact_Db,Register_db,Order_db
import os.path
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def new(request):
    total=Order_db.objects.all().count()
    contact=contact_Db.objects.all().count()
    return render(request,"index.html",{'total':total,'contact':contact})
def addcate(request):
    return render(request,"addcategory.html")
def savejewelcat(request):
    if request.method =="POST":
        Category_Na =request.POST.get('Category_Name')
        Product_Na = request.POST.get('Product_name')
        price = request.POST.get('Price')
        Descri = request.POST.get('Description')
        img=request.FILES['Cat_img']
        obj=Jewelcate_Db(Category_Name=Category_Na,Product_Name=Product_Na,Price=price,Description=Descri,Cat_img=img)
        obj.save()
        return redirect(addcate)
def displaycate(request):
    data=Jewelcate_Db.objects.all()
    return render(request,"displaycaegories.html",{'data':data})
def editcatego(request,cat_id):
    data = Jewelcate_Db.objects.get(id=cat_id)
    if request.method =="POST":
        data.Category_Name = request.POST.get('Category_Name')
        data.Product_Name = request.POST.get('Product_Name')
        data.Price = request.POST.get('Price')
        data.Description = request.POST.get('Description')
        if 'Cat_img' in request.FILES:
            old_img=data.Cat_img.path
            if os.path.exists(old_img):
                os.remove(old_img)
            data.Cat_img=request.FILES['Cat_img']
        data.save()
        return redirect('displaycate')
    return render(request,"editcategories.html",{'data':data})
def delcate(request,cat_id):
    x=Jewelcate_Db.objects.filter(id=cat_id)
    x.delete()
    return redirect('displaycate')
def ornaments(request):
    return render(request,"ornamentsadd.html")
def saveornaments(request):
    if request.method =="POST":
        Category_Name=request.POST.get('Category_Name')
        Product_Name=request.POST.get('Product_Name')
        Price=request.POST.get('Price')
        Description=request.POST.get('Description')
        weight=request.POST.get('weight')
        item_gross_weight=request.POST.get('item_gross_weight')
        item_net_weight=request.POST.get('item_net_weight')
        chain_length=request.POST.get('chain_length')
        Ornaments_img=request.FILES['Ornaments_img']
        Ornaments_img2=request.FILES['Ornaments_img2']
        obj=Ornaments_Db(Category_Name= Category_Name,Product_Name= Product_Name,Price=Price, Description= Description,weight=weight,item_gross_weight=item_gross_weight,item_net_weight= item_net_weight,chain_length=chain_length,Ornaments_img=Ornaments_img,Ornaments_img2=Ornaments_img2)
        obj.save()
        return redirect('ornaments')
def displayornaments(request):
    data=Ornaments_Db.objects.all()
    return render(request,"displayornaments.html",{'data':data})
def editornaments(request,orn_id):
    data=Ornaments_Db.objects.get(id=orn_id)
    if request.method =="POST":
        data.Category_Name=request.POST.get('Category_Name')
        data.Product_Name=request.POST.get('Product_Name')
        data.Price=request.POST.get('Price')
        data.Description=request.POST.get('Description')
        data.weight=request.POST.get('weight')
        data.item_gross_weight=request.POST.get('item_gross_weight')
        data.item_net_weight=request.POST.get('item_net_weight')
        data.chain_length=request.POST.get('chain_length')
        if 'Ornaments_img' in request.FILES:
            orn_img=data.Ornaments_img.path
            if os.path.exists(orn_img):
                os.remove(orn_img)
            data.Ornaments_img=request.FILES['Ornaments_img']
        if 'Ornaments_img2' in request.FILES:
            orn_img2 = data.Ornaments_img2.path
            if os.path.exists(orn_img2):
                os.remove(orn_img2)
            data.Ornaments_img2=request.FILES['Ornaments_img2']
        data.save()
        return redirect('displayornaments')
    return render(request,"editornament.html",{'data':data})
def delorn(request,orn_id):
    x=Ornaments_Db.objects.filter(id=orn_id)
    x.delete()
    return redirect('displayornaments')
def admin1(request):
    return render(request, "adminlogin.html")
def adminlog(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username__contains=username).exists():
            x = authenticate(username=username, password=password)

            if x is not None:
                login(request, x)
                request.session["username"] = username
                request.session["password"] = password
                return redirect("new")
            else:
                return redirect("admin1")
        else:
            return redirect("admin1")

    return render(request, "adminlogin.html")
def display_contacts(request):
    data= contact_Db.objects.all()
    return render(request, "displaycontacts.html",{'data':data})
def deletecontacts(request,con_id):
    x = contact_Db.objects.filter(id=con_id)
    x.delete()
    return redirect('display_contacts')
def display_register(request):
    data=Register_db.objects.all()
    return render(request,"displayuser.html",{'data':data})
def delete_register(request,user_id):
    x = Register_db.objects.filter(id=user_id)
    x.delete()
    return redirect('display_register')
def orderdisplay(request):
    data=Order_db.objects.all()
    return render(request,"orderdisplay.html",{'data':data})

