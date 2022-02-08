from django.shortcuts import render, redirect
from bands.models import Band
from bands.forms import BandForm
# Create your views here.


def bands(request):
    # Récupérer toutes les groupes
    bands = Band.objects.all()
    context = {'bands': bands}

    return render(request, 'bands/bands.html', context)


def band_detail(request, band_id):
    # Récupérer un groupe en particulier grâce à son id (clé primaire)
    band = Band.objects.get(id=band_id)
    context = {'band': band}

    return render(request, 'bands/band_detail.html', context)

def add_band(request):
    form = BandForm()
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bands:index')
    context = {'form': form}

    return render(request, 'bands/add_band.html', context)

def update_band(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('bands:detail', band.id)
    else :
        form = BandForm(instance=band)
    context = {'form': form, 'band': band}

    return render(request, 'bands/update_band.html', context)

def delete_band(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == "POST":
        band.delete()
        return redirect('bands:index')
    context = {'band': band}

    return render(request, 'bands/delete_band.html', context)
