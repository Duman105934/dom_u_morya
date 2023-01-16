from django.shortcuts import render, get_object_or_404
from houses.models import House
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from houses.forms import HousesFilterForm
from django.db.models import Q


def houses_list(request):
    houses = House.objects.filter(active=True)
    form = HousesFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            houses = houses.filter(price__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            houses = houses.filter(price__lte=form.cleaned_data["max_price"])
        if form.cleaned_data["query"]:
            houses = houses.filter(
                Q(description__icontains=form.cleaned_data["query"]) |
                Q(name__icontains=form.cleaned_data["query"]))
        if form.cleaned_data["ordering"]:
            houses = houses.order_by(form.cleaned_data["ordering"])
    return render(request, "houses/houses_list.html", {"houses": houses, "form": form})


def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id, active=True)
    form = OrderForm(request.POST or None, initial={"house": house})

    if request.method == "POST":
        if form.is_valid():
            form.save()
            url = reverse("house", kwargs={"house_id": house_id})
            return HttpResponseRedirect(f"{url}?sent=1")

    return render(request, "houses/house_detail.html", {
        "house": house,
        "form": form,
        "sent": request.GET.get("sent")
        })