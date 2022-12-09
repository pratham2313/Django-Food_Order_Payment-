from django.contrib import admin
from kali.models import Contact
from kali.models import additalians
from kali.models import addsouths
from kali.models import addtocart
from kali.models import addpanjabis
from kali.models import registration
from kali.models import paydetails
# Register your models here.

admin.site.register(Contact)
admin.site.register(additalians)
admin.site.register(addsouths)
admin.site.register(addtocart)
admin.site.register(addpanjabis)
admin.site.register(registration)
admin.site.register(paydetails)