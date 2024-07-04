from django.db import models

# Modelo de Tienda. 
class Comprador(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=60)
    nro_documento = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Comprador"
        verbose_name_plural = "Compradores"
        ordering = ["nombre"]
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    nro_documento = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ["nombre"]
    

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    nro_item = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]





