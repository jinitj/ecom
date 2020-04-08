from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer,Cart


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        #customer_created=Customer.objects.filter(user=instance)
        #Cart.objects.create(cart_identifier=Customer.objects.filter(user=instance))


@receiver(post_save, sender=Customer)
def create_customer_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(cart_identifier=instance)