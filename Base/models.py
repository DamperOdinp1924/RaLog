from django.db import models
from django.contrib.auth.models import User

class Aerolineas(models.Model):
    Name = models.TextField(max_length=20)
    def __str__(self):
        return self.Name

class Origen(models.Model):
    Name = models.TextField(max_length=20)
    def __str__(self):
        return self.Name

class Destino(models.Model):
    Name = models.TextField(max_length=20)
    def __str__(self):
        return self.Name

class Cliente(models.Model):
    Name = models.TextField(max_length=30)
    Email = models.EmailField(max_length=30)
    Number = models.CharField(max_length=10)
    def __str__(self):
        return self.Name  # Cambiado a CharField para almacenar números de teléfono

class Carga(models.Model):
    Name = models.TextField(max_length=10)
    def __str__(self):
        return self.Name

class TT(models.Model):
    Name = models.TextField(max_length=20)
    def __str__(self):
        return self.Name

class TarifasAerolineasFrutas(models.Model):
    FechaActualizacion = models.DateTimeField(null=True)
    ResponsableActualizacion = models.ForeignKey(User, on_delete=models.CASCADE)
    Aerolineas = models.ForeignKey(Aerolineas, on_delete=models.CASCADE, related_name="ATarifas")
    Origen = models.ForeignKey(Origen, on_delete=models.CASCADE, related_name="Origen")
    Destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name="Destino")
    Conexion = models.TextField(max_length=10)
    Carga = models.ForeignKey(Carga, on_delete=models.CASCADE, related_name="Carga")
    DSalida = models.TextField(max_length=10)
    Min = models.DateField()
    kg_100 = models.IntegerField()
    kg_300 = models.IntegerField()
    kg_500 = models.IntegerField()
    kg_1000 = models.IntegerField()
    kg_3000 = models.IntegerField()
    PMC = models.IntegerField()
    PMCKG = models.IntegerField()
    FS = models.IntegerField()
    OTHERS = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.FechaActualizacion} - {self.Aerolineas} - {self.Destino}'

class RegistroKg(models.Model):
    actualizacion = models.ForeignKey(TarifasAerolineasFrutas, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    kg_100 = models.IntegerField()
    kg_300 = models.IntegerField()
    kg_500 = models.IntegerField()
    kg_1000 = models.IntegerField()
    kg_3000 = models.IntegerField()

    def __str__(self):
        return f'{self.fecha_registro} - {self.actualizacion} - {self.kg_100} - {self.kg_300} - {self.kg_500} - {self.kg_1000} - {self.kg_3000}'
