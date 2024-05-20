from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductoForm, MarcaForm, StockForm
from .models import Producto, MarcaProducto, Stock

def index(request):
    return render(request, 'aplicacion/index.html')

def buscar(request):
    productos = Producto.objects.all()
    marcas = MarcaProducto.objects.all()
    stocks = Stock.objects.all()
    context = {
        'productos': productos,
        'marcas': marcas,
        'stocks': stocks
    }
    return render(request, 'aplicacion/buscar.html', context)

def agregar_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']
            nombre = form.cleaned_data['marca']
            precio = form.cleaned_data['precio']

            marca_obj, created = MarcaProducto.objects.get_or_create(nombre=nombre, tipo_producto=producto, precio=precio)
            if created:
                messages.success(request, 'Marca agregada exitosamente.')
            else:
                messages.info(request, 'La marca ya existe.')
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

            stock_obj.cantidad += cantidad
            stock_obj.save()
            messages.success(request, 'Stock agregado exitosamente.')
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
            messages.success(request, 'Producto agregado exitosamente.')
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
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('index')
    return render(request, 'eliminar/eliminar_producto.html', {'productos': productos})

def eliminar_marca(request):
    marcas = MarcaProducto.objects.all()
    if request.method == 'POST':
        marca_id = request.POST.get('marca_id')
        marca = get_object_or_404(MarcaProducto, pk=marca_id)
        marca.delete()
        messages.success(request, 'Marca eliminada exitosamente.')
        return redirect('index')
    return render(request, 'eliminar/eliminar_marca.html', {'marcas': marcas})

def eliminar_stock(request):
    stocks = Stock.objects.all()
    if request.method == 'POST':
        stock_id = request.POST.get('stock_id')
        stock = get_object_or_404(Stock, pk=stock_id)
        cantidad_a_eliminar = int(request.POST.get('cantidad', 0))

        if cantidad_a_eliminar <= 0 or cantidad_a_eliminar > stock.cantidad:
            messages.error(request, 'Cantidad inválida.')
            return render(request, 'eliminar/eliminar_stock.html', {'stocks': stocks})

        stock.cantidad -= cantidad_a_eliminar
        if stock.cantidad == 0:
            stock.delete()
        else:
            stock.save()

        messages.success(request, 'Stock eliminado exitosamente.')
        return redirect('index')
    return render(request, 'eliminar/eliminar_stock.html', {'stocks': stocks})

