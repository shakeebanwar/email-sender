# Create your models here.
from django.db import models
from rest_framework import serializers
from django.contrib import admin
from tinymce.models import HTMLField

userAcountStatus = (
    ('True','True'),
    ('False','False')
    
)

rewardStatus = (

    ('pending','pending'),
    ('done','done')

)


class emailRecord(models.Model):

    
    Fname=models.CharField(max_length=255, default="")
    Lname=models.CharField(max_length=255, default="")
    Email=models.EmailField(max_length=255, default="")
    mobile=models.CharField(max_length=20, default="")
    sendstatus=models.CharField(max_length=10, default="False")


  
    def __str__(self):
        return self.Email



    

###Search Critarea
class adminemailRecord(admin.ModelAdmin):
    search_fields = ['Fname','Lname','Email','mobile','sendstatus']




class DiscountPrice(models.Model):
    price = models.IntegerField(default=0)
    discountlink=models.TextField(default="")
    
    def __str__(self):
        return str(self.price)


# For normal user
class UserSignup(models.Model):

    uid = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=255, default="")
    lname=models.CharField(max_length=255, default="")
    email=models.EmailField(max_length=255, default="")
    password=models.TextField(max_length=500, default="")
    mobile=models.CharField(max_length=20, default="")
    profile= models.ImageField(upload_to='users/',default="users/dummy.jpg")
    totalnoofappointment = models.IntegerField(default=0)
    account_Status = models.CharField(max_length=10,choices=userAcountStatus, default="True") 
    def __str__(self):
        return self.fname


###Search  Critarea
class adminUserSignup(admin.ModelAdmin):
    search_fields = ['fname','lname','email','mobile']

    


class UserReferalRecord(models.Model):
    rid = models.AutoField(primary_key=True)
    userReferenceId = models.ForeignKey(UserSignup , on_delete=models.CASCADE,blank=True,null=True,related_name='userreferece')
    userClickId = models.ForeignKey(UserSignup , on_delete=models.CASCADE,blank=True,null=True,related_name='userclick')
    discountprice = models.IntegerField(default=0)
    discountlink=models.TextField(default="")
    status = models.CharField(max_length=10,choices=rewardStatus, default="pending") 


    def __str__(self):
        return self.userReferenceId.fname



###Search  Critarea
class adminUserReference(admin.ModelAdmin):
    search_fields = ['userReferenceId__fname','userClickId__fname','discountprice','status']



class Rating(models.Model):
    stars = models.FloatField(default=0)
    review=models.TextField(default="")
    datetime = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    author = models.ForeignKey(UserSignup , on_delete=models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return str(self.stars)


###Search  Critarea
class adminRating(admin.ModelAdmin):
    search_fields = ['stars','author__fname','author__lname']




class landingContent(models.Model):
    content = HTMLField()


class referalCompaign(models.Model):
    content = HTMLField()



    
class emailReferalrecord(models.Model):
    userReference =  models.EmailField(max_length=255, default="")
    userRecieve = models.EmailField(max_length=255, default="")
    referFirstname = models.CharField(max_length=255, default="")
    recieverFirstname = models.CharField(max_length=255, default="")
    creation =  models.DateField(blank=True,null=True)
