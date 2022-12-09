from asyncio.windows_events import NULL
from email.headerregistry import Address
from pyexpat import model
from django.db import models
from django.db.models import Model
from django.urls import reverse


# Create your models here.

# Model field references documantation.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class registration(models.Model):
    id=models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phonenum = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    
    

    def __str__(self):
        return self.firstname

class additalians(models.Model):
    iid=models.AutoField(primary_key=True)
    iname = models.CharField(max_length=50)
    iprize=models.IntegerField(default=NULL)
    itemimage = models.ImageField(blank=True,null=True,upload_to="")

    def get_absolute_url(self):
        return reverse("Item details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.iname


class addpanjabis(models.Model):
    pid=models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    pprize=models.IntegerField(default=NULL)
    pimage = models.ImageField(blank=True,null=True,upload_to="")

    def get_absolute_url(self):
        return reverse("Item details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.pname



class addsouths(models.Model):
    sid=models.AutoField(primary_key=True)
    sname = models.CharField(max_length=50)
    sprize=models.IntegerField(default=NULL)
    southimage = models.ImageField(blank=True,null=True,upload_to="")

    def get_absolute_url(self):
        return reverse("Item details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.sname


class addtocart(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.CharField(max_length=50,null=True)
    atcid=models.CharField(max_length=50)
    atcname = models.CharField(max_length=50)
    atcprize=models.IntegerField(default=NULL)
    atcimage = models.ImageField(blank=True,null=True,upload_to="")

    def get_absolute_url(self):
        return reverse("Item details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.atcname

class paydetails(models.Model):
    payid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    
    

    def __str__(self):
        return self.name        

