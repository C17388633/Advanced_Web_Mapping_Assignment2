from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
# for the airports
from django.template import loader

from . import models

# For Signup page
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# For seeing templates offline
from django.shortcuts import render
from django.core import serializers
import json

# Create your views here.
from .models import Airport
from .resources import AirportResource


@login_required
def update_location(request):
    try:
        user_profile = models.Profile.objects.get(user=request.user)
        if not user_profile:
            raise ValueError("Can't get User details")

        point = request.POST["point"].split(",")
        point =[float(part) for part in point]
        point = Point(point, srd=4326)

        user_profile.last_location = point
        user_profile.save()

        return JsonResponse({"message": f"Set location tp {point.wkt}."}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


# Signup page
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

from tablib import Dataset

# ourairports.org import csv file
def simple_upload(request):
    if request.method == 'POST':
        airport_resource = AirportResource()
        dataset = Dataset()
        new_airports = request.FILES['myfile']

        imported_data = dataset.load(new_airports.read())
        result = airport_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            airport_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'world/simple_upload.html')


def airports(request):
    airport_results = Airport.objects.all()
    context = {
        'airport_results': airport_results
    }
    return render(request, "airports.html", context)