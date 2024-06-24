from django.db import models

# Create your models here.
class User(models.Model):
    userfullname = models.CharField(max_length=225, primary_key=True)
    userid = models.CharField(max_length=30)
    useremail = models.EmailField()
    userphone = models.IntegerField()

class Login(models.Model):
    username = models.CharField(max_length=225, primary_key=True)
    password = models.CharField(max_length=225)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

class Admin(models.Model):
    adminid = models.AutoField(primary_key=True)
    adminemail = models.EmailField()
    adminname = models.CharField(max_length=50)
    adminuser = models.CharField(max_length=30)
    adminpassword = models.CharField(max_length=12)

class Member(models.Model):
    memberid = models.AutoField(primary_key=True)
    memberemail = models.EmailField()
    membername = models.CharField(max_length=50)
    memberpassword = models.CharField(max_length=12)

class Registration(models.Model):
    registrationid = models.AutoField(primary_key=True)
    userfullname = models.ForeignKey(User, on_delete=models.CASCADE)
    studid = models.CharField(max_length=30)
    studphone = models.IntegerField()
    club = models.CharField(max_length=30)
    registration_status = models.CharField(max_length=30, default="Pending")

class Booking(models.Model):
    bookingid = models.AutoField(primary_key=True)
    equipment = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=30, default="Pending")

class Chart(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    image = models.ImageField(upload_to='orgmember', null=True, blank=True)



