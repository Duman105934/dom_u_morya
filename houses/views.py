from django.shortcuts import render
from houses.models import House


def houses_list(request):
    houses = House.objects.all()
    for house in houses:
        print(house.name, house.price)
    return render(request, "houses/houses_list.html", {"houses": houses})