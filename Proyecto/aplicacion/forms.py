from django import forms
from .models import Producto, MarcaProducto, Stock

class ProductoForm(forms.Form):
    producto = forms.CharField(max_length=100)

class MarcaForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    marca = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class StockForm(forms.Form):
    marca = forms.ModelChoiceField(queryset=MarcaProducto.objects.all())
    cantidad = forms.IntegerField()
