from django.contrib import admin
from account.models import UserAddress, UserBankAccount

# Register your models here.
admin.site.register(UserBankAccount)
admin.site.register(UserAddress)
