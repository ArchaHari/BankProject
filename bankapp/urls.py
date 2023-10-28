from django.urls import path
from .views import *

urlpatterns=[
    path("register/",register),
    path("login/",login),
    path("home/",home),
    path("profile",profile),
    path("edit/<int:id>",editdetails),
    path("editpic/<int:id>",editpic),
    path("addamount/<int:id>",addamount),
    path("success/",success),
    path("withdrawamount/<int:id>",withdrawamount),
    path("withdrawsuccess/",withdrawsuccess),
    path("checkbalance/<int:id>",checkbalance),
    path("showbalance/",showbalance),
    path("ministatement/<int:id>",ministatement),
    path("depositstatement/",depositstatement),
    path("withdrawstatement/",withdrawstatement),
    path("newsfeed/",newsfeed),
    path("newsdisplay/",newsdisplay),
    path("adminnewsdisplay/",adminnewsdisplay),
    path("newsdelete/<int:id>",newsdelete),
    path("newsedit/<int:id>",newsedit),
    path("adminlogin/",adminlogin),
    path("adminprofile/",adminprofile),
    path("wishlist/<int:id>",wishlist),
    path("wishlistdisplay/",wishlistdisplay),
    path("wishremove/<int:id>",wishremove),
    path("addedtowishlist/",addedtowishlist),
    path("alreadyinwishlist/", alreadyinwishlist),
    path("logout/",logout_view),
    path("forgotpassword/",forgot_password),
    path("change/<int:id>",change_password),
    path("moneytransfer/<int:id>",moneytransfer),
    path("transfersuccess/",transfersuccess)



]