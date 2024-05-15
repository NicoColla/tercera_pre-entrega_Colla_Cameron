from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class MarcaProducto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_producto})"

class Stock(models.Model):
    marca = models.ForeignKey(MarcaProducto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
