from django.shortcuts import render,redirect,get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from .form import AddAerolineas, AddDestins, AddOrigins, AddRates, AddCliente, AddCarga
from .models import Aerolineas, Destino, Origen, TarifasAerolineasFrutas, Cliente, Carga
from django.http import JsonResponse

# Create your views here.
def test(request):
    return render(request, 'Home.html')



# def entry(request):
#     if request.method == 'POST':
#         # Procesar el formulario de registro
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # Crear un nuevo usuario si el formulario es válido
#             user = form.save()
#             # Iniciar sesión con el nuevo usuario
#             login(request, user)
#             return redirect('Home.html')
#         else:
#             # El formulario no es válido, volver a mostrarlo con errores
#             return render(request, 'Entry.html', {'formSignup': form})
#     else:
#         # Mostrar el formulario de registro en una solicitud GET
#         form = UserCreationForm()
#     return render(request, 'Entry.html', {'formSignup': form})





# def entry(request):
#     error = ''  # Define la variable error aquí para que esté disponible en todas las ramas
#     if request.method == 'POST':
#         # Procesar el formulario de registro aquí
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Autenticar al usuario después de registrarse
#             login(request, user)
#             # Redirigir al usuario a la página de inicio
#             return redirect('home')
#         else:
#             error = 'Username already dfddf'  # Actualiza el valor de error en caso de error en el formulario
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'Entry.html', {'formSignup': form, 'error': error})

def entry(request):
    if request.method == 'POST':
        if 'registrar' in request.POST:
            form = UserCreationForm(request.POST)
            if request.POST['password1'] == request.POST['password2']: 
                try:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                except Exception as e:
                    return HttpResponseServerError(f'Error al crear el usuario: {str(e)}')
            else:
                return render(request, 'Entry.html', {'form': form, 'form2': AuthenticationForm(), 'error': 'Registration error'})

        elif 'ingresar' in request.POST:
            form2 = AuthenticationForm(request, data=request.POST)
            if form2.is_valid():
                user = form2.get_user()
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'Entry.html', {'form': UserCreationForm(), 'form2': form2, 'error': 'Login error'})

    # Si es una solicitud GET o no se envió un formulario, muestra ambos formularios
    form = UserCreationForm()
    form2 = AuthenticationForm()
    return render(request, 'Entry.html', {'form': form, 'form2': form2})

def signout(request):
    logout(request)
    return redirect('Entry.html')




# def home(request):
#     AirlinesR = Aerolineas.objects.all()
#     FAerolinea = AddAerolineas()
#     show_supplier = False

#     if request.method == 'POST':
#         if 'salir' in request.POST:
#             logout(request)
#             return redirect('entry')
#         elif 'AddSupplier' in request.POST:
#             FAerolinea = AddAerolineas(request.POST)
#             if FAerolinea.is_valid():
#                 new_airline = FAerolinea.save(commit=False)
#                 new_airline.save()
#                 # Configura la variable para mostrar la sección "Añadir Proveedor"
#                 show_supplier = True

#     # Pasa la variable de contexto show_supplier
#     return render(request, 'Home.html', {'AirlinesR': AirlinesR, 'FAerolinea': FAerolinea, 'show_supplier': show_supplier})


def home(request):
    if request.method == 'POST':
        if 'salir' in request.POST:
            logout(request)
            return redirect('entry')
        elif 'proveedorer' in request.POST:
            return redirect('suppliers')
    return render(request, 'Home.html')


from django.contrib import messages


def suppliers(request):
    VAerolineas = Aerolineas.objects.all()
    FAerolinea = AddAerolineas()
    VDestins = Destino.objects.all()
    FDestino = AddDestins()
    VOrigen = Origen.objects.all()
    FOrigen = AddDestins()
    VCarga = Carga.objects.all()
    FCarga = AddCarga()

    if request.method == 'POST':
        if 'AddSupplier' in request.POST:
            FAerolinea = AddAerolineas(request.POST)
            if FAerolinea.is_valid():
                new_airline = FAerolinea.save()
                messages.success(request, 'Aerolínea agregada exitosamente.')
                return redirect('suppliers')
            else:
                messages.error(request, 'Hubo un error al agregar la aerolínea. Por favor, verifica los campos.')
        elif 'eliminar_Aerolinea' in request.POST:
            try:
                Aerolinea_id = int(request.POST.get('Aerolinea_id'))
                DAerolinea = get_object_or_404(Aerolineas, id=Aerolinea_id)
                DAerolinea.delete()
                messages.success(request, 'Aerolínea eliminada exitosamente.')
                return redirect('suppliers')
            except Exception as e:
                print(f"Error al eliminar la aerolínea: {e}")
                messages.error(request, 'Hubo un error al eliminar la aerolínea.')
                return HttpResponseServerError("Error interno al eliminar la aerolínea.")
        elif 'AddDestin' in request.POST:
            FDestino = AddDestins(request.POST)
            if FDestino.is_valid():
                new_Destin = FDestino.save()
                messages.success(request, 'Aerolínea agregada exitosamente.')
                return redirect('suppliers')
            else:
                messages.error(request, 'Hubo un error al agregar el destino, Por favor, verifica los campos.')
        elif 'eliminar_Destin' in request.POST:
            try:
              Destino_id = int(request.POST.get('Destino_id'))
              DDestino = get_object_or_404(Destino, id=Destino_id)
              DDestino.delete()
              messages.success(request, 'Destino eliminado exitosamente')
              return redirect('suppliers')
            except Exception as e:
                print(f'Error al eliminar destino: {e}')
                messages.error(request,'Hubo un error al eliminar destino')
                return HttpResponse("Error interno al eliminar destino")
        elif 'AddOrigin' in request.POST:
            FOrigen = AddOrigins(request.POST)
            if FOrigen.is_valid():
                new_Destin = FOrigen.save()
                messages.success(request, 'Aerolínea agregada exitosamente.')
                return redirect('suppliers')
            else:
                messages.error(request, 'Hubo un error al agregar el destino, Por favor, verifica los campos.')
        elif 'eliminar_Origin' in request.POST:
            try:
              Origen_id = int(request.POST.get('Origen_id'))
              DOrigen = get_object_or_404(Origen, id=Origen_id)
              DOrigen.delete()
              messages.success(request, 'Destino eliminado exitosamente')
              return redirect('suppliers')
            except Exception as e:
                print(f'Error al eliminar destino: {e}')
                messages.error(request,'Hubo un error al eliminar destino')
                return HttpResponse("Error interno al eliminar destino")
        elif 'addCarga' in request.POST:
            FCarga = AddCarga(request.POST)
            if FCarga.is_valid():
                FCarga.save()
                return redirect('suppliers')
            else:
              messages.error(request,'Hubo error al crear el tipo de carga')
        elif 'eliminar_carga' in request.POST:
            try:
                carga_id = int(request.POST.get('carga_id'))
                DCarga = get_object_or_404(Carga,id=carga_id)
                DCarga.delete()
                messages.success(request, 'Tipo carga eliminada satisfactoriamente')
                return redirect('suppliers')
            except Exception as e:
                print(f'Error al eliminar tipo carga: {e}')
                messages.error(request,'Error al eliminar tipo carga')
                return HttpResponse('error al eliminar tipo carga')
    return render(request, 'Supplier.html', {'VAerolineas': VAerolineas, 'FAerolinea': FAerolinea, 'VDestins':VDestins, 'FDestino':FDestino, 'FOrigen':FOrigen, 'VOrigen':VOrigen, 'VCarga':VCarga, 'FCarga':FCarga})


def ratesAir(request):
    # Inicializar el formulario vacío
    FRates = AddRates()
    
    # Obtener todos los registros de la base de datos
    VRates = TarifasAerolineasFrutas.objects.all()

    # Filtrar la consulta según los parámetros de filtro en la solicitud POST
    if request.method == 'POST':
        # Verificar si se envió el formulario para agregar tarifas
        if 'AddRates' in request.POST:
            FRates = AddRates(request.POST)
            if FRates.is_valid():
                FRates.save()
                messages.success(request, 'Tarifa agregada correctamente.')
            else:
                messages.error(request, 'Hubo un error al agregar la tarifa. Verifica los campos.')
                print(FRates.errors)  # Esto imprimirá los errores del formulario a la consola de Django

        # Verificar si se solicitó eliminar una tarifa
        elif 'eliminar_Rates' in request.POST:
            Rates_id = int(request.POST.get('Rates_id'))
            DRates = get_object_or_404(TarifasAerolineasFrutas, id=Rates_id)
            DRates.delete()
            messages.success(request, 'Tarifa eliminada correctamente.')
            return redirect('ratesAir')

        # Verificar si se solicitó editar una tarifa
        elif 'editar_Rates' in request.POST:
            Rates_id = int(request.POST.get('Rates_id'))
            E1Rates = get_object_or_404(TarifasAerolineasFrutas, id=Rates_id)
            Erates = AddRates(request.POST, instance=E1Rates)
            if Erates.is_valid():
                Erates.save()
                messages.success(request, 'Tarifa editada correctamente.')
                return redirect('ratesAir')

        # Resto del código para filtrar

    return render(request, 'RRatesAirlines.html', {'FRates': FRates, 'VRates': VRates})


# import pandas as pd

# def importar_tarifas(request):
#     TarifasAerolineasFrutas.objects.all().delete()  # Opcional: eliminar registros existentes antes de la importación

#     # Ruta al archivo Excel, ajusta según tu caso
#     ruta_archivo = 'ruta/del/archivo/excel.xlsx'

#     try:
#         df = pd.read_excel(ruta_archivo)
#         for index, row in df.iterrows():
#             TarifasAerolineasFrutas.objects.create(
#                 FechaActualizacion=row['FechaActualizacion'],
#                 ResponsableActualizacion_id=row['ResponsableActualizacion'],
#                 Aerolineas_id=row['Aerolineas'],
#                 Origen_id=row['Origen'],
#                 Destino_id=row['Destino'],
#                 Conexion=row['Conexion'],
#                 Carga_id=row['Carga'],
#                 DSalida=row['DSalida'],
#                 Min=row['Min'],
#                 kg_100=row['kg_100'],
#                 kg_300=row['kg_300'],
#                 kg_500=row['kg_500'],
#                 kg_1000=row['kg_1000'],
#                 kg_3000=row['kg_3000'],
#                 PMC=row['PMC'],
#                 PMCKG=row['PMCKG'],
#                 FS=row['FS'],
#                 OTHERS=row['OTHERS']
#             )
#         mensaje = "Importación exitosa."
#     except Exception as e:
#         mensaje = f"Error durante la importación: {str(e)}"

#     return render(request, 'importar_tarifas.html', {'mensaje': mensaje})

# def suppliers(request):
#     aerolineas = Aerolineas.objects.all()
#     form = AddAerolineas()

#     if request.method == 'POST':
#         form = AddAerolineas(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('suppliers')  # Puedes cambiar 'suppliers' por el nombre de tu vista

#     return render(request, 'Supplier.html', {'aerolineas': aerolineas, 'form': form})

# def edit_supplier(request, pk):
#     aerolinea = get_object_or_404(Aerolineas, pk=pk)
#     form = AddAerolineas(instance=aerolinea)

#     if request.method == 'POST':
#         form = AddAerolineas(request.POST, instance=aerolinea)
#         if form.is_valid():
#             form.save()
#             return redirect('suppliers')  # Puedes cambiar 'suppliers' por el nombre de tu vista

#     return render(request, 'EditSupplier.html', {'form': form, 'aerolinea': aerolinea})

# def delete_supplier(request, pk):
#     aerolinea = get_object_or_404(Aerolineas, pk=pk)

#     if request.method == 'POST':
#         aerolinea.delete()
#         return redirect('suppliers')  # Puedes cambiar 'suppliers' por el nombre de tu vista

#     return render(request, 'DeleteSupplier.html', {'aerolinea': aerolinea})


# def entry(request):
#   if request.method == 'GET':
#     return render(request, 'Entry.html',{
#     'form': UserCreationForm,
#     'form2': AuthenticationForm
#   })
#   else:
#     if 'registrar' in request.POST:
#       if request.POST['password1'] == request.POST['password2']:
#         #Register user
#         try:
#           user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
#           user.save()
#           login(request, user)
#           HttpResponse('Correct created user')
#           return redirect('home')

#         except:
#           return render(request, 'Entry.html',{
#           'form': UserCreationForm,
#           'error': 'Username already exists'})
#       return render(request, 'Entry.html',{
#         'form': UserCreationForm,
#         'error': 'Password do not match'})
#     elif 'ingresar' in request.POST:
#           user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#           print(request.POST)
      
#           if user is None:
#             return render(request, 'Entry.html',{
#             'form2': AuthenticationForm,
#             'error': 'Username or password is incorrect'
#           })
#           else:
#             login(request, user)
#             return redirect('home')



# def signin(request):
#   if request.method == 'GET':
#     return render(request, 'Entry.html',{
#       'form2': AuthenticationForm
#   })
#   else:
#     user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#     print(request.POST)

#     if user is None:
#       return render(request, 'Entry.html',{
#       'form2': AuthenticationForm,
#       'error': 'Username or password is incorrect'
#     })
#     else:
#       login(request, user)
#       return redirect('home')

# def signout(request):
#     logout(request)
#     return redirect('Entry.html')

# def home(request):
#     render(request, 'Home.html')

# def entry(request):
#   if request.method == 'POST':
#     if 'registrar' in request.POST:
#       return render(request, 'Entry.html',{
#       'form': UserCreationForm
#       })
#     else:
#       if request.POST['password1'] == request.POST['password2']:
#         #Register user
#         try:
#           user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
#           user.save()
#           login(request, user)
#           HttpResponse('Correct created user')
#           return redirect('home')

#         except:
#           return render(request, 'Entry.html',{
#           'form': UserCreationForm,
#           'error': 'Username already exists'})
#       return render(request, 'Entry.html',{
#         'form': UserCreationForm,
#         'error': 'Password do not match'})

