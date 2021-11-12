from django.shortcuts import render

from warehouse.models import Category


def show_genres(request):
    return render(request, "warehouse/genres.html", {'genres': Category.objects.all()})
