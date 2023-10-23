from django import forms
from .models import TarifasAerolineasFrutas, Aerolineas, Destino,Origen, Cliente, Carga




class AddAerolineas(forms.ModelForm):
    class Meta:
        model = Aerolineas
        fields = '__all__'

class AddDestins(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class AddCarga(forms.ModelForm):
    class Meta:
        model = Carga
        fields = '__all__'



class AddOrigins(forms.ModelForm):
    class Meta:
        model = Origen
        fields = '__all__'

class AddRates(forms.ModelForm):
    class Meta:
        model = TarifasAerolineasFrutas
        fields = '__all__'
        labels = {
            'FechaActualizacion': 'Fecha de Actualización',
            'ResponsableActualizacion': 'Responsable de Actualización',
            # ... Etiquetas para otros campos ...
        }



class AddCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = {'Name','Email','Number'}

