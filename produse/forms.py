from django import forms
from .models import Products

# class ProductsForm(forms.Form):
#     product = forms.CharField(label="Produs", max_length=100)
#     bought = forms.BooleanField(required=False,)

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product', 'bought']

