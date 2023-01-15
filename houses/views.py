from django.shortcuts import render, get_object_or_404
from houses.models import House
from orders.forms import OrderForm


def houses_list(request):
    houses = House.objects.all()
    return render(request, "houses/houses_list.html", {"houses": houses})


def house_detail(request, house_id):
    form = OrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    house = get_object_or_404(House, id=house_id)
    return render(request, "houses/house_detail.html", {"house": house, "form": form})