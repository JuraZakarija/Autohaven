# Generated by Django 3.1.2 on 2021-01-30 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['title', 'id'])),
                ('title', models.CharField(max_length=255)),
                ('make', models.CharField(choices=[('Abarth', 'Abarth'), ('Alfa Romeo', 'Alfa Romeo'), ('Aston Martin', 'Aston Martin'), ('Audi', 'Audi'), ('Bentley', 'Bentley'), ('BMW', 'BMW'), ('Bugatti', 'Bugatti'), ('Cadillac', 'Cadillac'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Citroën', 'Citroën'), ('Dacia', 'Dacia'), ('Daewoo', 'Daewoo'), ('Daihatsu', 'Daihatsu'), ('Dodge', 'Dodge'), ('Donkervoort', 'Donkervoort'), ('DS', 'DS'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Fisker', 'Fisker'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Hummer', 'Hummer'), ('Hyundai', 'Hyundai'), ('Infiniti', 'Infiniti'), ('Iveco', 'Iveco'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('KTM', 'KTM'), ('Lada', 'Lada'), ('Lamborghini', 'Lamborghini'), ('Lancia', 'Lancia'), ('Land Rover', 'Land Rover'), ('Landwind', 'Landwind'), ('Lexus', 'Lexus'), ('Lotus', 'Lotus'), ('Maserati', 'Maserati'), ('Maybach', 'Maybach'), ('Mazda', 'Mazda'), ('McLaren', 'McLaren'), ('Mercedes-Benz', 'Mercedes-Benz'), ('MG', 'MG'), ('Mini', 'Mini'), ('Mitsubishi', 'Mitsubishi'), ('Morgan', 'Morgan'), ('Nissan', 'Nissan'), ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('Renault', 'Renault'), ('Rolls-Royce', 'Rolls-Royce'), ('Rover', 'Rover'), ('Saab', 'Saab'), ('Seat', 'Seat'), ('Skoda', 'Skoda'), ('Smart', 'Smart'), ('SsangYong', 'SsangYong'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo')], max_length=50)),
                ('price', models.PositiveIntegerField(blank=True)),
                ('mileage', models.PositiveIntegerField(blank=True)),
                ('power', models.PositiveIntegerField(blank=True)),
                ('location', models.CharField(max_length=255)),
                ('county', models.CharField(choices=[('Zagrebačka', 'Zagrebačka'), ('Krapinsko-zagorska', 'Krapinsko-zagorska'), ('Sisačko-moslavačka', 'Sisačko-moslavačka'), ('Karlovačka', 'Karlovačka'), ('Varaždinska', 'Varaždinska'), ('Koprivničko-križevačka', 'Koprivničko-križevačka'), ('Bjelovarsko-bilogorska', 'Bjelovarsko-bilogorska'), ('Primorsko-goranska', 'Primorsko-goranska'), ('Ličko-senjska', 'Ličko-senjska'), ('Virovitičko-podravska', 'Virovitičko-podravska'), ('Požeško-slavonska', 'Požeško-slavonska'), ('Brodsko-posavska', 'Brodsko-posavska'), ('Zadarska', 'Zadarska'), ('Osječko-baranjska', 'Osječko-baranjska'), ('Šibensko-kninska', 'Šibensko-kninska'), ('Vukovarsko-srijemska', 'Vukovarsko-srijemska'), ('Splitsko-dalmatinska', 'Splitsko-dalmatinska'), ('Istarska', 'Istarska'), ('Dubrovačko-neretvanska', 'Dubrovačko-neretvanska'), ('Međimurska', 'Međimurska'), ('Grad Zagreb', 'Grad Zagreb')], max_length=50)),
                ('color', models.CharField(blank=True, max_length=50)),
                ('year', models.PositiveSmallIntegerField(blank=True)),
                ('engine', models.CharField(choices=[('petrol', 'benzin'), ('diesel', 'diesel'), ('electric', 'električni'), ('hybrid', 'hibrid')], max_length=20)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
