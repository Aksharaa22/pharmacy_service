from django.contrib import admin
from PharmSupply.models import Register
# Register your models here.
@admin.register(Register)
class Register(admin.ModelAdmin):
    pass