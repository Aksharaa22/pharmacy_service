from django.contrib import admin

# Register your models here.
from . models import Image,Payment


admin.site.register(Image)
admin.site.register(Payment)