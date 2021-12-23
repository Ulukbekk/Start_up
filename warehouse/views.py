from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from warehouse.forms import AddMaterialForm, AddCategoryForm, MaterialSearchForm, UpdateMaterialForm
from warehouse.models import Category, Material


def all_materials(request):
    materials = Material.objects.all()
    form = MaterialSearchForm(request.POST or None)
    paginator = Paginator(materials, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        page_obj = Material.objects.filter(category__icontains=form['category'].value(),
                                            title__icontains=form['title'].value(),
                                            color__icontains=form['color'].value(),
                                            shade__icontains=form['shade'].value())

    context = {
        'form': form,
        'materials': page_obj
    }
    return render(request, 'warehouse/all_material.html', context)


def add_material(request):
    if request.method == 'POST':
        form = AddMaterialForm(request.POST)
        print(request.POST.getlist('category'))
        if form.is_valid():
            form.save()
            return redirect('all_materials')
    form = AddMaterialForm()
    context = {
        'form': form
    }
    return render(request, 'warehouse/add_material.html', context)


def update_material(request, pk):
    materials = Material.objects.filter(id=pk).first()
    form = UpdateMaterialForm(instance=materials)
    if request.method == 'POST':
        form = UpdateMaterialForm(request.POST, instance=materials)
        if form.is_valid():
            form.save()
            return redirect('all_materials')
    form = UpdateMaterialForm(instance=materials)
    context = {
        'form': form,
        'materials': materials
    }
    return render(request, 'warehouse/update_material.html', context)


def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_material')
    form = AddCategoryForm()
    context = {
        'form': form
    }
    return render(request, 'warehouse/add_category.html', context)
