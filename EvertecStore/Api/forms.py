from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['customer_name', 'customer_email', 'customer_mobile']
