from import_export.admin import ImportExportModelAdmin
from django.contrib.gis import admin
from .models import WorldBorder

admin.site.register(WorldBorder, admin.GeoModelAdmin)

from .models import Airport

@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    pass