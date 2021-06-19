from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Register)
admin.site.register(Image)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(cart)
admin.site.register(ShippingAddress)