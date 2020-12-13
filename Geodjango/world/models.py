from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

# Auto-generated `LayerMapping` dictionary for WorldBorder model
worldborder_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    last_location = models.PointField(editable=False, blank=True, null = True, default = None)

    def __str__(self):
        return f"{self.user}"

    #
    # Signal
    #
    @receiver(post_save, sender=get_user_model())
    def manage_user_profile(sender, instance, created, **kwargs):
        try:
            my_profile = instance.profile
            my_profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(user=instance)


# airports
class Airport(models.Model):
    id = models.IntegerField(primary_key=True)
    ident = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.IntegerField()
    continent = models.CharField(max_length=3)
    iso_country = models.CharField(max_length=50)
    iso_region = models.CharField(max_length=50)
    municipal = models.CharField(max_length=50)
    scheduled_service = models.CharField(max_length=50)
    gps_code = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=50)
    local_code = models.CharField(max_length=50)
    home_link = models.CharField(max_length=200)
    wikipedia_link = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)

    def __str__(self):
        return self.name


