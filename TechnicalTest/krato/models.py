from django.db import models


class Ciudad(models.Model):
    """Modelo de Ciudad."""
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre',)


class Tienda(models.Model):
    """Modelo de Ciudad. Relación Many-to-Many con Usuario mediante usuario_set.
    Relación One-To-Many con Ciudad."""
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=150)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)


class Usuario(models.Model):
    """Modelo de Usuario. Relación Many-to-Many con Tienda."""
    nombre = models.CharField(max_length=50)
    cedula = models.PositiveIntegerField()
    residencia = models.CharField(max_length=150, blank=True)
    tiendas = models.ManyToManyField(Tienda)

    def __str__(self):
        return "{}: {}".format(self.nombre, self.cedula)
