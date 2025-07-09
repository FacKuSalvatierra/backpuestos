from django.db import models
from django.core.validators import MinValueValidator

class Integrante(models.Model):
    """
    Modelo para representar a las personas que pueden estar en guardias
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"
        ordering = ['apellido', 'nombre']
        unique_together = ['nombre', 'apellido']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Guardia(models.Model):
    """
    Modelo para representar una guardia
    """
    numero = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Número de guardia",
        help_text="Número de guardia"
    )
    fecha = models.DateField(verbose_name="Fecha de la guardia")
    integrantes = models.ManyToManyField(
        Integrante,
        verbose_name="Integrantes"
    )
    activa = models.BooleanField(default=True, verbose_name="Activa")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "Guardia"
        verbose_name_plural = "Guardias"
        ordering = ['fecha', 'numero']
        unique_together = ['numero', 'fecha']
    
    def __str__(self):
        return f"Guardia {self.numero} - {self.fecha}"
    
    @property
    def total_integrantes(self):
        return self.integrantes.count()
