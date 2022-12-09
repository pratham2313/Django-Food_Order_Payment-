from ast import For
from django.conf import settings
from atexit import register
import email
from email import message
from email.headerregistry import Address
from email.mime import image
from itertools import product
from mailbox import MaildirMessage
from multiprocessing import context
from re import X
from sre_parse import State
from tkinter import Image
from unicodedata import name
from urllib import response
from django.forms import PasswordInput
from django.shortcuts import render, HttpResponse
from datetime import datetime
from kali.models import Contact, addpanjabis, paydetails
from kali.models import additalians
from django.contrib import messages    # from messages django documentation
from kali.models import addsouths
from kali.models import addtocart
from kali.models import addpanjabis
from kali.models import registration
from kali.models import paydetails
from django.contrib.auth.models import User 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
import kali
import uuid
import random
import string
import razorpay
from datetime import date

from nill.settings import RAZORPAY_API_KEY

# Create your views here.


def index(request):
    all=request.user
    username=all.username
    print(username)
    context = { 'username':username}
    
    if request.user.is_superuser==True:
        all=request.user
        firstname=all.first_name
        print(firstname)
        return render(request, 'test.html',context)            
    else:
        
        return render(request, 'ctest.html',context)
    
    # return HttpResponse("This is homepage of kali")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")
    
def home(request):
    all=request.user
    username=all.username
    print(username)
    context = { 'username':username}
    if request.user.is_superuser==True:
        
        context = { 'username':username}
        return render(request, 'test.html',context)            
    else:
        return render(request, 'ctest.html',context)



def loginuser(request):
    var="admin"
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            
            if request.user.is_superuser==True:
                all=request.user
                username=all.username
                print(username)
                context = { 'username':username}
                
                return render(request,'test.html',context)
            else:
                all=request.user
                username=all.username
                print(username)
                context = { 'username':username}
                return render(request, 'ctest.html',context)
        else:
            messages.error(request,'Invalid Username and Password')
            return render(request,'login.html')     
 
            

    return render(request, 'login.html')        

    

def logoutuser(request):
    logout(request)
    return render(request,'login.html')

def regiform(request):
    
    return render(request, 'register.html')

def regi(request):
    if request.method == "POST":
        username=request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        password2=request.POST.get('password2')
        email = request.POST.get('email')
        
        allmail=User.objects.filter(username=username)
        print(allmail)
        count=len(allmail)
        if count != 0:
            messages.error(request, 'This Username is alredy Exist Try Another Username')
        else: 
            if password==password2 :
                user = User.objects.create_user(username, email, password)
                user.first_name=firstname
                user.last_name=lastname

                user.save()
                print(user.id)
                messages.success(request, 'Your Account Created Sccessfully Login Here')
                return render(request, 'login.html')
            else :
                messages.error("Your Password Don't Match to Confirm Password") 
                return render(request,'register.html')  
        
        
            
    return render(request,'register.html')

def punjabi(request):
    allpan=addpanjabis.objects.all()
    print(allpan)
    context = { 'allpan':allpan}
    return render(request, 'punjabi.html',context)
    # return HttpResponse("This is book page from services section")

def itemview(request):
    
    return render(request, 'addtocart.html')

def south(request):
    allsouth=addsouths.objects.all()
    print(allsouth)
    context = { 'allsouth':allsouth}
    return render(request, 'south.html',context)


def italian(request):
    allitalian=additalians.objects.all()
    context = { 'allitalian':allitalian}
    
    
    return render(request, 'italian.html',context)


def atcart(request):
    user=request.user
    u_id=user.id
    allcart=addtocart.objects.filter(uid=u_id)
    details=paydetails.objects.latest('payid')
    print(details)
    
    count=len(allcart)
    sum=0
    for a in allcart:
        i=a.atcprize
        sum=sum+i
    GST=int((sum*18)/100)+sum
    context = { 'allcart':allcart,
    'count':count,
    'sum':sum,
    'GST':GST}
    return render(request, 'addtocart.html',context)

def aftergoandcheckout(request):
    allcart=addtocart.objects.all()
    count=len(allcart)
    sum=0
    for a in allcart:
        i=a.atcprize
        sum=sum+i
    GST=int((sum*18)/100)+sum
    context = { 'allcart':allcart,
    'count':count,
    'sum':sum,
    'GST':GST}
    return render(request, 'addressform.html',context)

def atcartdelete(request,atc_id):
    allcartd=addtocart.objects.filter(id=atc_id)
    allcartd.delete()
    user=request.user
    u_id=user.id
    allcart=addtocart.objects.filter(uid=u_id)
    count=len(allcart)
    sum=0
    for a in allcart:
        i=a.atcprize
        sum=sum+i
    GST=int((sum*18)/100)+sum
    context = { 'allcart':allcart,
    'count':count,
    'sum':sum,
    'GST':GST}
    
    return render(request, 'addtocart.html',context)




def addtocartsouth(request):
    if request.method == "POST":
        addcart = addtocart()
        addcart.uid=request.POST.get('userid')
        addcart.atcid=request.POST.get('atcid')
        addcart.atcname = request.POST.get('atcname')
        addcart.atcprize = request.POST.get('atcprize')
        
        addcart.atcimage= request.POST.get('atcimage')    
        
        addcart.save()
        messages.success(request, 'Submitted Successfully.')
        allsouth=addsouths.objects.all()
        print(allsouth)
        context = { 'allsouth':allsouth}
    return render(request, 'south.html',context)
    
       
    
def addtocartita(request):
    if request.method == "POST":
        addcart = addtocart()
        addcart.uid=request.POST.get('userid')
        addcart.atcid=request.POST.get('atcid')
        addcart.atcname = request.POST.get('atcname')
        addcart.atcprize = request.POST.get('atcprize')
        
        addcart.atcimage= request.POST.get('atcimage')    
        
        addcart.save()
        
        messages.success(request, 'Submitted Successfully.')
        allitalian=additalians.objects.all()
        context = { 'allitalian':allitalian}
    
    
        return render(request, 'italian.html',context)
    
    
def addtocartpan(request):
    if request.method == "POST":
        addcart = addtocart()
        addcart.uid=request.POST.get('userid')
        addcart.atcid=request.POST.get('atcid')
        addcart.atcname = request.POST.get('atcname')
        addcart.atcprize = request.POST.get('atcprize')
        
        addcart.atcimage= request.POST.get('atcimage')    
        
        addcart.save()
        
        messages.success(request, 'Submitted Successfully.')
        allpan=addpanjabis.objects.all()
        print(allpan)
        context = { 'allpan':allpan}
    return render(request, 'punjabi.html',context)
    
    

def additalian(request):
    if request.user.is_superuser==True:
        if request.method == "POST":
            produ = additalians()
            produ.iname = request.POST.get('italianname')
            if len(request.FILES)!=0:

                produ.itemimage= request.FILES.get('italianimage')
            produ.iprize = request.POST.get('italianprize')

        # Additem = additalians(iname=iname,itemimage=itemimage)    
        
            produ.save()
        # Popup after click submit
            messages.success(request, 'Submitted Successfully.')
    
        
        return render(request, 'additalian.html')
    return render(request, 'ctest.html')
def addsouth(request):
    if request.user.is_superuser==True:
       if request.method == "POST":
           
           prod = addsouths()
        
           prod.sname = request.POST.get('southname')
           if len(request.FILES)!=0:
               
               prod.southimage= request.FILES.get('southimage')

           prod.sprize = request.POST.get('southprize')

           # southitem = addsouths(sname=sname,southimage=southimage)    
        
           prod.save()
        
        # Popup after click submit
           messages.success(request, 'Submitted Successfully.')
       return render(request, 'addsouth.html') 
    return render(request, 'ctest.html')   
        
def addpanjabi(request):
    if request.user.is_superuser==True:
        if request.method == "POST":
            prodp = addpanjabis()
        
            prodp.pname = request.POST.get('pname')
            if len(request.FILES)!=0:
                
                prodp.pimage= request.FILES.get('pimage')

            prodp.pprize = request.POST.get('pprize')

        # southitem = addsouths(sname=sname,southimage=southimage)    
        
            prodp.save()
        # Popup after click submit
            messages.success(request, 'Submitted Successfully.')
        
        return render(request, 'addpanjabi.html')   
    return render(request, 'ctest.html')     
        

def contact(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        all=Contact.objects.latest('name')
        
        # Popup after click submit
        messages.success(request, 'Submitted Successfully.')

    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

def aftersave(request):
    if request.method == "POST":
        all=request.user
        u_id=all.id
        allcart=addtocart.objects.filter(uid=u_id)
        count=len(allcart)
        sum=0
        for a in allcart:
            i=a.atcprize
            sum=sum+i
        GST=int((sum*18)/100)+sum
        context = { 'allcart':allcart,
        'count':count,
        'sum':sum,
        'GST':GST}
        pay=paydetails()
        pay.name = request.POST.get('name')
        pay.email = request.POST.get('email')
        pay.address1 = request.POST.get('address1')
        pay.address2 = request.POST.get('address2')
        pay.city = request.POST.get('city')
        pay.state = request.POST.get('state')
        pay.pincode = request.POST.get('pincode')
        pay.save()
        all=paydetails.objects.all()
        order_p= request.POST.get('payprice')
        order_a=int(order_p)
        order_amount=GST*100
        
        order_currency= "INR"
        client = razorpay.Client(auth=("rzp_test_izbfCqhO8Zyndt", "ZKLl6U0V3gmN0I5APLXjWNiO"))
        payment=client.order.create({'amount':order_amount,'currency': order_currency,'payment_capture':1})
        id=payment['id']
        order_id=id
        
        context={
            'allcart':allcart,
            'count':count,
            'sum':sum,
            'GST':GST,
            'amounta':order_a,
            'amount':order_amount,
            'order_id':order_id,
            'api_key':RAZORPAY_API_KEY,
            
        }
        messages.success(request, 'Your Account Created Sccessfully Login Here')
        return render(request, 'placeorder.html',context)    
    
def payment(request):
    if request.method == 'POST':
        allcart=addtocart.objects.all()
        count=len(allcart)
        sum=0
        for a in allcart:
            i=a.atcprize
            sum=sum+i
        GST=int((sum*18)/100)+sum
        
        
        order_paisa= request.POST.get('payprice')
        order_amount=order_paisa*100
        print(order_amount)
        order_currency= "INR"
        client = razorpay.Client(auth=("rzp_test_izbfCqhO8Zyndt", "ZKLl6U0V3gmN0I5APLXjWNiO"))
        payment=client.order.create({'amount':order_amount,'currency': order_currency,'payment_capture':1})
        id=payment['id']
        order_id=id
        
        context={
            'allcart':allcart,
            'count':count,
            'sum':sum,
            'GST':GST,
            'amount':order_amount,
            'order_id':order_id,
            'api_key':RAZORPAY_API_KEY,
            
        }
        
        
        return render(request,'invoice.html',context)
        
def invo(request):
    all=request.user
    username=all.username
    details=paydetails.objects.latest('payid')
    today = date.today()
    u_id=all.id
    allcart=addtocart.objects.filter(uid=u_id)
    print(details)
    # id = uuid.uuid1()
    # invoid=id.variant
    count=len(allcart)
    sum=0
    for a in allcart:
        i=a.atcprize
        sum=sum+i
    GST=int((sum*18)/100)+sum
    tax=GST-sum
    
    def ran_gen(size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    invoid=ran_gen(8, "AEIOSUMA23")
    print(username)
    context = { 
    'username':username,
    'details':details,
    'today':today,
    'count':count,
    'sum':sum,
    'GST':GST,
    'allcart':allcart,
    'tax':tax,
    'invoid':invoid}

    return render(request,'invoice.html',context)        
       
    

        

        