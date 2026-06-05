from django.shortcuts import render, redirect
from .models import DestinoTuristico
from .forms import DestinoTuristicoForm

# Create your views here.
def lista_destinos(request):
    destinos = DestinoTuristico.objects.all()
    return render(request, 'turismo/lista_destinos.html', {'destinos': destinos})

def agregar_destino(request):

    if request.method == 'POST':
        form = DestinoTuristicoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_destinos')

    else:
        form = DestinoTuristicoForm()

    return render(
        request,
        'turismo/agregar_destino.html',
        {'form': form}
    )

def editar_destino(request, id):
    
    destino = DestinoTuristico.objects.get(id=id)

    if request.method == 'POST':
        form = DestinoTuristicoForm(
            request.POST,
            instance=destino
        )

        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
        
    else:
        form = DestinoTuristicoForm(instance=destino)

    return render(
        request,
        'turismo/editar_destino.html',
        {'form': form}
    )

def eliminar_destino(request, id):

    destino = DestinoTuristico.objects.get(id=id)

    destino.delete()

    return redirect('lista_destinos')