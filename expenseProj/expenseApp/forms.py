from django import forms
from .models import ExpenseModel, Transaction

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = '__all__'
        widgets = {
            'username': forms.HiddenInput(),
        }



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'account_fk': forms.HiddenInput(),
        }