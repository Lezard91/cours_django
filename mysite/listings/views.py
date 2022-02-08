from django.shortcuts import render, redirect
from listings.models import Listing
from listings.forms import ListingForm
# Create your views here.


def index(request):
    listings = Listing.objects.all()
    context = {'listingList': listings}

    return render(request, 'listings/index.html', context)


def detail(request, id):
    listing = Listing.objects.get(id=id)
    context = {'listing': listing}

    return render(request, 'listings/detail.html', context)


def add(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listings:index')
    context = {'form': form}

    return render(request, 'listings/add.html', context)

def update_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings:detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    context = {'form' : form, 'listing': listing}

    return render(request, 'listings/update_listing.html', context)

def delete_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        listing.delete()
        return redirect('listings:index')
    context = {'listing': listing}

    return render(request, 'listings/delete_listing.html', context)