import uuid
import math

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from .choices import MAKE, COUNTY, ENGINE

# Create your models here.
class Listing(TimeStampedModel, models.Model):
    class Meta:
        ordering = ["-created"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from=["title", "id"])
    title = models.CharField(max_length=255)
    make = models.CharField(max_length=50, choices=MAKE)
    price = models.PositiveIntegerField(blank=True)
    mileage = models.PositiveIntegerField(blank=True)
    power = models.PositiveIntegerField(blank=True)
    location = models.CharField(max_length=255)
    county = models.CharField(max_length=50, choices=COUNTY)
    color = models.CharField(max_length=50, blank=True)
    year = models.PositiveSmallIntegerField(blank=True)
    engine = models.CharField(max_length=20, choices=ENGINE)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):  # new
        return self.title

    def get_absolute_url(self):  # new
        return reverse("listing-detail", kwargs={"slug": self.slug})

    def get_price_euros(self):
        return math.ceil(self.price / (100.0 * 7.57)) * 100

    def get_power_in_horsepower(self):
        return round(self.power * 1.341)
