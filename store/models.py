from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    delivery_address = models.CharField(max_length=265)
    
    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length =350)
    photo = models.ImageField(blank=False, upload_to='product_images')
    price=models.IntegerField(blank=False, default=500)
    description = models.TextField()

    # def get_absolute_url(self):
    #     return reverse("products:product-list", kwargs={"itemid": self.id})

    def __str__(self):
        return self.name

class Cart(models.Model):
    #cart_id = models.CharField(max_length=265, primary_key=True)
    cart_identifier = models.OneToOneField(Customer,on_delete = models.CASCADE)
    
    total = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)

class CartElement(models.Model):
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
