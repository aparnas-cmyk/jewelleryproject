from django.db import models
class contact_Db(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email= models.EmailField(max_length=100, null=True, blank=True)
    Subject= models.CharField(max_length=100, null=True, blank=True)
    Message= models.CharField(max_length=100, null=True, blank=True)

class Register_db(models.Model):
    Full_Name= models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirm_password= models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
# Create your models here.
class cart_db(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    product_name= models.CharField(max_length=100, null=True, blank=True)
    quantity= models.IntegerField(null=True, blank=True)
    price= models.IntegerField(null=True, blank=True)
    total_price= models.IntegerField(null=True, blank=True)
    product_image= models.ImageField(upload_to='images/', null=True, blank=True)

class Order_db(models.Model):
    first_Name = models.CharField(max_length=100, null=True, blank=True)
    last_Name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    total_price= models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)