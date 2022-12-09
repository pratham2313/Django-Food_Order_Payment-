from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.views import View
from kali import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='kali'),
    path("home", views.home, name='home'),
    path("loginuser", views.loginuser, name='loginuser'),
    path("logoutuser", views.logoutuser, name='logoutuser'),
    path("regiform", views.regiform, name='regiform'),
    path("regi", views.regi, name='regi'),
    path("about", views.about, name='about'),
    path("punjabi", views.punjabi, name='punjabi'),
    path("south", views.south, name='south'),
    path("italian", views.italian, name='italian'),
    path("contact", views.contact, name='contact'),
    path("additalian", views.additalian, name='additalian'),
    path("addsouth", views.addsouth, name='addsouth'),
    path("addpanjabi", views.addpanjabi, name='addpanjabi'),
    path("addtocartsouth", views.addtocartsouth, name='addtocartsouth'),
    path("addtocartita", views.addtocartita, name='addtocartita'),
    path("addtocartpan", views.addtocartpan, name='addtocartpan'),
    path("itemview", views.itemview, name='itemview'),
    path("atcart", views.atcart, name='atcart'),
    path("atcartdelete/<atc_id>", views.atcartdelete, name='atcartdelete'),
    path("payment", views.payment, name='payment'),
    path("aftersave", views.aftersave, name='aftersave'),
    path("aftergoandcheckout", views.aftergoandcheckout, name='aftergoandcheckout'),
    path("invo", views.invo, name='invo'),
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
