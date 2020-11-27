from django import forms
from .models import  Transaction

class TransactionForm(forms.Form):
    description = forms.CharField(max_length=200, required=False)
    mobile = forms.CharField(max_length=11, required=False)
    email = forms.EmailField(required=False)
    amount = forms.IntegerField(required=False)
