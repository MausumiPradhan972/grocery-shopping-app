from django.db import models


# Create your models here.
class Signin_model(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    def __str__(self):
      return self.name
class contact_model(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    sub=models.CharField(max_length=20)
    message=models.CharField(max_length=20)
    def __str__(self):
       return f"{self.name}-{self.sub}"
class Product(models.Model):
   CATEGORY_CHOICES=[
      ('packaged','Packaged'),
      ('fruit','Fruit'),
      ('cooking','Cooking'),
      ('dairy','Dairy')
   ]
   name=models.CharField(max_length=50,unique=True)
   price=models.CharField()
   image=models.ImageField(upload_to='products/',null=True,blank=True)
   category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='packaged')
   def __str__(self):
      return self.name
class Order(models.Model):
   created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
   total_price=models.DecimalField(max_digits=10,decimal_places=2)
   def __str__(self):
      return f"Order{self.id}"
class OrderItem(models.Model):
   order=models.ForeignKey(Order,on_delete=models.CASCADE)
   product=models.ForeignKey('product',on_delete=models.CASCADE)
   image=models.ImageField(upload_to="",null=True,blank=True)
   name=models.CharField(max_length=20)
   quantity=models.IntegerField()
   price=models.IntegerField()
   
   
