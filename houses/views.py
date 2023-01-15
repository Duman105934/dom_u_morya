from django.shortcuts import render


def houses_list(request):
    return render(request, "houses/houses_list.html")