from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, MarcaForm, StockForm
from .models import Producto, MarcaProducto, Stock

def index(request):
    return render(request, 'aplicacion/index.html')

def buscar_producto(request):
    return render(request, 'buscar_producto.html')

def agregar_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']
            nombre = form.cleaned_data['marca']
            precio = form.cleaned_data['precio']

            marca_obj, _ = MarcaProducto.objects.get_or_create(nombre=nombre, tipo_producto=producto, precio=precio)
            marca_obj.save()

            return redirect('index')
    else:
        form = MarcaForm()
    return render(request, 'agregar/agregar_marca.html', {'form': form})


def agregar_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            cantidad = form.cleaned_data['cantidad']
            stock_obj, created = Stock.objects.get_or_create(marca=marca)

            if not created:
                stock_obj.cantidad += cantidad
                stock_obj.save()
            else:
                stock_obj.cantidad = cantidad
                stock_obj.save()

            return redirect('index')
    else:
        form = StockForm()
    return render(request, 'agregar/agregar_stock.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nombre_producto = form.cleaned_data['producto']
            Producto.objects.get_or_create(nombre=nombre_producto)
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'agregar/agregar_producto.html', {'form': form})

def eliminar_producto(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        return redirect('index')
    return render(request, 'eliminar/eliminar_producto.html', {'productos': productos})

def eliminar_marca(request):
    marcas = MarcaProducto.objects.all()
    if request.method == 'POST':
        marca_id = request.POST.get('marca_id')
        marca = get_object_or_404(MarcaProducto, pk=marca_id)
        marca.delete()
        return redirect('index')
    return render(request, 'eliminar/eliminar_marca.html', {'marcas': marcas})

def eliminar_stock(request):
    stocks = Stock.objects.all()
    if request.method == 'POST':
        stock_id = request.POST.get('stock_id')
        stock = get_object_or_404(Stock, pk=stock_id)
        cantidad_a_eliminar = int(request.POST.get('cantidad', 0))
        
        if cantidad_a_eliminar > 0 and cantidad_a_eliminar <= stock.cantidad:
            stock.cantidad -= cantidad_a_eliminar
            stock.save()
            return redirect('index')
        else:
            error_message = "La cantidad ingresada es inválida o excede la cantidad disponible en el stock."
            return render(request, 'eliminar/eliminar_stock.html', {'stocks': stocks, 'error_message': error_message})

    return render(request, 'eliminar/eliminar_stock.html', {'stocks': stocks})
