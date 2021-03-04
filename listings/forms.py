from django.forms import ModelForm

from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "make",
            "mileage",
            "price",
            "location",
            "county",
            "power",
            "color",
            "year",
            "engine",
            "photo_main",
            "photo_1",
            "photo_2",
            "photo_3",
            "photo_4",
            "photo_5",
            "photo_6",
        ]

        labels = {
            "title": "Naziv",
            "make": "Marka",
            "mileage": "Kilometraža",
            "price": "Cijena",
            "location": "Lokacija",
            "county": "Županija",
            "power": "Snaga",
            "color": "Boja",
            "year": "Godina",
            "engine": "Tip motora",
            "photo_main": "Glavna slika",
            "photo_1": "Slika 1",
            "photo_2": "Slika 2",
            "photo_3": "Slika 3",
            "photo_4": "Slika 4",
            "photo_5": "Slika 5",
            "photo_6": "Slika 6",
        }
