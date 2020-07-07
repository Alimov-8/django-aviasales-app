from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest2 = Destination()
    dest3 = Destination()

    dest1.name = "Brazil"
    dest1.desc = "Football"
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2.name = "Uzbekistan"
    dest2.desc = "Best Place"
    dest2.price = 888
    dest2.img = 'destination_2.jpg'
    dest2.offer = True

    dest3.name = "Korea"
    dest3.desc = "INCHEON"
    dest3.price = 1500
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})