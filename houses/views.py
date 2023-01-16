from django.shortcuts import render, get_object_or_404
from houses.models import House
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def houses_list(request):
    houses = House.objects.all()
    return render(request, "houses/houses_list.html", {"houses": houses})


def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
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