from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail

# Create your views here.

def register(request):
    if(request.method=='POST'):
        a=regform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['firstname']
            ln=a.cleaned_data['lastname']
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            acnum="15"+str(ph)
            img=a.cleaned_data['image']
            pn=a.cleaned_data['pin']
            rn=a.cleaned_data['rpin']
            if pn==rn:
                b=regmodel(firstname=fn,lastname=ln,username=un,email=em,phone=ph,image=img,pin=pn,balance=0,acnum=int(acnum))
                b.save()
                subject="Your Account has been Created"
                message=f"Your new Account Number is {acnum}"
                email_from="archaammu100@gmail.com"
                email_to=em
                send_mail(subject,message,email_from,[email_to])
                return redirect(login)
            else:
                return HttpResponse("password doesn't match")
        else:
            return HttpResponse("registration failed")
    return render(request,"registration.html")

def login(request):
    if request.method=="POST":
        a=logform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            pn=a.cleaned_data['pin']
            b=regmodel.objects.all()
            for i in b:
                if i.username==un and i.pin==pn:
                    #global
                    request.session['id']=i.id
                    return redirect(profile)
            else:
                return HttpResponse("Login Failed!")
    return render(request,"login.html")

def home(request):
    return render(request,"homepage.html")

def profile(request):
    try:
        id1=request.session['id']
        a=regmodel.objects.get(id=id1)
        img=str(a.image).split('/')[-1]
        return render(request,"profile.html",{'a':a,'img':img})
    except:
        return redirect(login)

def editdetails(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.save()
        return redirect(profile)
    return render(request, 'editdetails.html', {'a': a})

def editpic(request,id):
    a=regmodel.objects.get(id=id)
    img=str(a.image).split('/')[-1]
    if request.method=='POST':
        a.username=request.POST.get('username')
        if len(request.FILES)!=0:
            if len(a.image)!=0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.save()
        return redirect(profile)
    return render(request,'editpic.html', {'a': a,'img':img})

def addamount(request,id):
    x=regmodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        pin=request.POST.get('pin')
        request.session['am']=am
        request.session['acnum']=x.acnum
        if pin==x.pin:
            x.balance+=int(am)
            x.save()
            b=addamountmodel(amount=am,uid=request.session['id'])
            b.save()
            return redirect(success)
        else:
            return HttpResponse("amount added failed")
    return render(request,"addamount.html")

def success(request):
    am=request.session['am']
    ac=request.session['acnum']
    return render(request,"success.html",{'am':am,'acnum':ac})

def withdrawamount(request,id):
    x=regmodel.objects.get(id=id)
    if request.method == 'POST':
        am=request.POST.get('amount')
        request.session['am']=am
        request.session['acnum']=x.acnum
        if(x.balance>=int(am)):
            x.balance-=int(am)
            x.save()
            b=withdrawmodel(amount=am,uid=request.session['id'])
            b.save()
            pin=request.POST.get('pin')
            if pin==x.pin:
                return redirect(withdrawsuccess)
            else:
                return HttpResponse("Password Incorrect")
        else:
            return HttpResponse("Insufficient Balance")
    return render(request,"withdrawamount.html")

def withdrawsuccess(request):
    am=request.session['am']
    ac=request.session['acnum']
    return render(request,"withdrawsuccess.html", {'am':am,'acnum':ac})

def checkbalance(request,id):
    x=regmodel.objects.get(id=id)
    if request.method == 'POST':
        request.session['balance']=x.balance
        request.session['acnum']=x.acnum
        pin=request.POST.get('pin')
        if pin==x.pin:
            return redirect(showbalance)
        else:
            return HttpResponse("Password Incorrect")
    return render(request, "checkbalance.html")

def showbalance(request):
    ac=request.session['acnum']
    bl=request.session['balance']
    return render(request,"showbalance.html",{'acnum':ac,'balance':bl})

def ministatement(request,id):
    x=regmodel.objects.get(id=id)
    pin=request.POST.get('pin')
    if request.method=='POST':
        if pin==x.pin:
            c=request.POST.get('choice')
            if c=="deposit":
                return redirect(depositstatement)
            elif c=="withdraw":
                return redirect(withdrawstatement)
        else:
            return HttpResponse("Incorrect Password")
    return render(request,"ministatement.html")

def depositstatement(request):
    a=addamountmodel.objects.all()
    id=request.session['id']
    return render(request,"depositstatement.html",{'a':a,'id':id})

def withdrawstatement(request):
    a=withdrawmodel.objects.all()
    id=request.session['id']
    return render(request,"withdrawstatement.html",{'a':a,'id':id})

def newsfeed(request):
    if request.method=='POST':
        a=newsfeedform(request.POST,request.FILES)
        if a.is_valid():
            tp=a.cleaned_data['topic']
            cn=a.cleaned_data['content']
            img=a.cleaned_data['image']
            b=newsfeedmodel(topic=tp,content=cn,image=img)
            b.save()
            return HttpResponse("News Feed Added Successfully")
        else:
            return HttpResponse("News Feed Adding Failed")
    return render(request,"newsfeed.html")

def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return redirect(adminprofile)
            else:
                return HttpResponse("admin login failed")
    return render(request,"adminlogin.html")

def adminprofile(request):
    return render(request,"adminprofile.html")

def newsdisplay(request):
    a=newsfeedmodel.objects.all()
    return render(request,'displaynewsfeed.html',{'a':a})

def adminnewsdisplay(request):
    a=newsfeedmodel.objects.all()
    return render(request,'admindisplaynewsfeed.html',{'a':a})

def newsedit(request,id):
    a=newsfeedmodel.objects.get(id=id)
    if request.method=='POST':
        a.topic=request.POST.get('topic')
        a.content=request.POST.get('content')
        a.save()
        return redirect(adminnewsdisplay)
    return render(request,'newsfeededit.html', {'a': a})

def newsdelete(request,id):
    a=newsfeedmodel.objects.get(id=id)
    a.delete()
    return redirect(adminnewsdisplay)

def wishlist(request,id):
    a=newsfeedmodel.objects.get(id=id)
    wishlist=wishlistmodel.objects.all()
    for i in wishlist:
        if i.newsid==a.id and i.uid==request.session['id']:
            return redirect(alreadyinwishlist)
    b=wishlistmodel(topic=a.topic,content=a.content,date=a.date,newsid=a.id,uid=request.session['id'])
    b.save()
    return redirect(addedtowishlist)

def addedtowishlist(request):
    return render(request,'addedtowishlist.html')

def alreadyinwishlist(request):
    return render(request,'alreadyinwishlist.html')

def wishlistdisplay(request):
    a=wishlistmodel.objects.all()
    id=request.session['id']
    return render(request,'wishlistdisplay.html',{'a':a,'id':id})

def wishremove(request,id):
    a=wishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(wishlistdisplay)

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect(home)

def forgot_password(request):
    a=regmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        ac=request.POST.get('acnum')
        for i in a:
            if(i.email==em and i.acnum==int(ac)):
                id=i.id
                subject="password change"
                message=f"http://127.0.0.1:8000/bankapp/change/{id}"
                frm="archaammu100@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("check email")
        else:
            return HttpResponse("sorry")
    return render(request,'forgotpassword.html')

def change_password(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('rpin')
        if p1==p2:
            a.pin=p1
            a.save()
            return HttpResponse("password changed")
        else:
            return HttpResponse("SORRY")
    return render(request,'change.html')

def moneytransfer(request,id):
    a=regmodel.objects.get(id=id)
    b=regmodel.objects.all()
    if request.method=='POST':
        nm=request.POST.get('username')
        an=request.POST.get('acnum')
        am=request.POST.get('amount')
        for i in b:
            if int(an)==i.acnum and nm==i.username:
                if a.balance>=int(am):
                    a.balance-=int(am)
                    i.balance+=int(am)
                    i.save()
                    a.save()
                    return redirect(transfersuccess)
                else:
                    return HttpResponse("insufficient balance")
        else:
            return HttpResponse("user not found")
    else:
        return render(request,"moneytransfer.html")

def transfersuccess(request):
    return render(request,"transfersuccess.html")


#authenticate is a function that checks the credentials and returns







