from django.db import models
class Jewelcate_Db(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Name= models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Cat_img=models.ImageField(upload_to="Cat_img",null=True, blank=True)

class Ornaments_Db(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Name= models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(null=True, blank=True)
    item_gross_weight=models.CharField(null=True, blank=True)
    item_net_weight=models.CharField(null=True, blank=True)
    chain_length = models.CharField(null=True, blank=True)
    Ornaments_img = models.ImageField(upload_to="Ornaments_img", null=True, blank=True)
    Ornaments_img2 = models.ImageField(upload_to="Ornaments_img2",null=True, blank=True)




# Create your models here.
