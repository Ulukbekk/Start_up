from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from warehouse.forms import AddMaterialForm, MaterialSearchForm, UpdateMaterialForm, IssueForm, ReceiveForm
from warehouse.models import Material


@login_required
def all_materials(request):
    materials = Material.objects.all()
    form = MaterialSearchForm(request.POST or None)
    paginator = Paginator(materials, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        page_obj = Material.objects.filter(category__icontains=form['category'].value(),
                                           title__icontains=form['title'].value(
        ),
            # color__icontains=form['color'].value(),
        )

    context = {
        'form': form,
        'materials': page_obj
    }
    return render(request, 'warehouse/all_material.html', context)


@login_required
def add_material(request):
    if request.method == 'POST':
        form = AddMaterialForm(request.POST)
        print(request.POST.getlist('category'))
        if form.is_valid():
            form.save()
            messages.success(request, 'Материал Добавлен')
            return redirect('all_materials')
    form = AddMaterialForm()
    context = {
        'form': form
    }
    return render(request, 'warehouse/add_material.html', context)


@login_required
def material_detail(request, pk):
    material = Material.objects.filter(id=pk)
    context = {
        'materials': material,
    }
    return render(request, 'warehouse/material_detail.html',
                  context)


@login_required
def update_material(request, pk):
    materials = Material.objects.filter(id=pk).first()
    form = UpdateMaterialForm(instance=materials)
    if request.method == 'POST':
        form = UpdateMaterialForm(request.POST, instance=materials)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные о Материале Были Изменены')
            return redirect('all_materials')
    form = UpdateMaterialForm(instance=materials)
    context = {
        'form': form,
        'materials': materials
    }
    return render(request, 'warehouse/update_material.html', context)


@login_required
def issue_items(request, pk):
    queryset = Material.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.amount -= instance.issue_quantity
        instance.issue_by = str(request.user)
        messages.success(request, "Issued SUCCESSFULLY. " + str(instance.amount) +
                         " " + str(instance.title) + "s now left in Store")
        instance.save()

        return redirect('/warehouse/material-detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": 'Issue ' + str(queryset.title),
        "queryset": queryset,
        "form": form,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, "warehouse/add_material.html", context)


@login_required
def receive_items(request, pk):
    queryset = Material.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.amount += instance.receive_quantity
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. " +
                         str(instance.amount) + " " + str(instance.title)+"s now in Store")

        return redirect('/warehouse/material-detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": 'Reaceive ' + str(queryset.title),
        "instance": queryset,
        "form": form,
        "username": 'Receive By: ' + str(request.user),
    }
    return render(request, "warehouse/add_material.html", context)
