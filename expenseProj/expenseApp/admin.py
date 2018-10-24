from django.contrib import admin

# Register your models here.
from .models import ExpenseModel, Transaction

admin.site.register(ExpenseModel)
admin.site.register(Transaction)
