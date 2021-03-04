import django_filters as filters

from .models import Listing


class ListingFilter(filters.FilterSet):
    def __init__(self, *args, **kwargs):
       super(ListingFilter, self).__init__(*args, **kwargs)
       self.filters['make'].label="Marka"
       self.filters['county'].label="Županija"
       self.filters['engine'].label="Motor"
       self.filters['mileage'].label="Kilometraža (min - max)"
       self.filters['price'].label="Cijena u kunama (min - max)"
       self.filters['power'].label="Snaga u kW (min - max)"
       self.filters['year'].label="Godina proizvodnje (min - max)"

    mileage = filters.RangeFilter()
    price = filters.RangeFilter()
    power = filters.RangeFilter()
    year = filters.RangeFilter()


    class Meta:
        model = Listing
        fields = ["make", "county", "engine", ]

        