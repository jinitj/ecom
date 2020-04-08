"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_details, name='product-list'),
    path("<int:myid>", views.productView, name="ProductView"),
    path('add-to-cart/<int:itemid>',views.add_to_cart,name="add-to-cart"),
    path('cart',views.cart_details,name='cart_details'),
    path('cart/remove-from-cart/<int:cart_element_id>',views.remove_from_cart,name='remove-from-cart'),

]
