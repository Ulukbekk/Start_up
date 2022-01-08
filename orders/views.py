import os
from django.contrib.auth import get_user_model
from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse, Http404, FileResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.utils import dateformat
from django.views.generic import FormView, DetailView

from core import settings
from orders.forms import ManagerBlankForm, WorkerEditForm, OrderSearchForm, ManagerBlankFilesForm
from orders.models import ManagerBlank, ManagerBlankFiles
from users.models import Account, Client
from warehouse.forms import MaterialSearchForm, AddMaterialForm
from django.contrib import messages
from time import gmtime, strftime
from num2words import num2words

from warehouse.models import Material


def home_page(request):
    # s_status = Status.objects.all().distinct()
    # s_type_order = Order.objects.all().distinct()
    # s_worker = Worker.objects.all().distinct()
    # s_condition = Condition.objects.all().distinct()
    position = request.user.position
    manage = Account.objects.filter(position='Менеджер')
    order_form = OrderSearchForm(request.POST or None)
    if str(position) == 'Менеджер' or 'Админ':
        orders = ManagerBlank.objects.filter().order_by('-date_created')
    else:
        orders = ManagerBlank.objects.filter(worker=position).order_by('-date_created')
    if request.method == 'POST':
        orders = ManagerBlank.objects.filter(
            title__icontains=order_form['title'].value(),
            status__icontains=order_form['status'].value(),
            condition__icontains=order_form['condition'].value(),
            worker__icontains=order_form['worker'].value(),
            order__icontains=order_form['order'].value(),
            # deadline__icontains=order_form['deadline'].value()
        )

    paginator = Paginator(orders, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'orders': page_obj,
        # 's_type_order': s_type_order,
        # 's_status': s_status,
        # 's_worker': s_worker,
        # 's_condition': s_condition,
        'position': position,
        'manage': manage,
        'order_form': order_form
    }
    return render(request, 'orders/home.html', context)


# def status_sort(request, pk):
#     status = Status.objects.filter(id=pk).first()
#     status_orders = ManagerBlank.objects.filter(status=status).order_by('-date_created')
#     context = {
#         'status_orders': status_orders,
#     }
#
#     return render(request, 'orders/sort.html', context)
#
#
# def worker_sort(request, pk):
#     worker = Worker.objects.filter(id=pk).first()
#     worker_orders = ManagerBlank.objects.filter(worker=worker).order_by('-date_created')
#     context = {
#         'worker_orders': worker_orders,
#     }
#
#     return render(request, 'orders/sort.html', context)
#
#
# def condition_sort(request, pk):
#     condition = Condition.objects.filter(id=pk).first()
#     condition_orders = ManagerBlank.objects.filter(condition=condition).order_by('-date_created')
#     context = {
#         'condition_orders': condition_orders,
#     }
#
#     return render(request, 'orders/sort.html', context)
#
#
# def order_sort(request, pk):
#     order = Order.objects.filter(id=pk).first()
#     type_orders = ManagerBlank.objects.filter(order=order).order_by('-date_created')
#     context = {
#         'type_orders': type_orders,
#     }
#
#     return render(request, 'orders/sort.html', context)


def add_order(request):
    if request.method == 'POST':
        form = ManagerBlankForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()
            messages.success(request, 'Заказ Добавлен')
            return redirect('home_page')
    form = ManagerBlankForm()
    context = {
        'form': form
    }
    return render(request, 'orders/add_order.html', context)


def add_files(request):
    if request.method == 'POST':
        form = ManagerBlankFilesForm(request.POST or None)
        files = request.FILES.getlist('files')
        file_list = []
        for f in files:
            new_file = ManagerBlankFiles(
                files=f
            )
            new_file.save()
            file_list.append(new_file.files.url)
        if form.is_valid():
            form.save()
        form = ManagerBlankFilesForm
        return render(request, 'orders/add_files.html', {'new_urls': file_list,
                                                         'form': form})
    else:
        return render(request, 'orders/add_files.html')


# def files(request):
#     if request.method == 'POST':
#         client = Client.objects.get(id=request.POST.get('client'))
#         status = Status.objects.get(id=request.POST.get('status'))
#         worker = Worker.objects.get(id=request.POST.get('worker'))
#         type_order = Order.objects.get(id=request.POST.get('order'))
#         condition = Condition.objects.get(id=request.POST.get('condition'))
#         form = ManagerBlankForm(request.POST, request.FILES)
#         files = request.FILES.getlist('files[]')
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.my_file = request.FILES.getlist('uploadfiles')
#             order.title = request.POST.get('title')
#             order.description = request.POST.get('description')
#             order.deadline = request.POST.get('deadline')
#             order.client = client
#             order.status = status
#             order.price = request.POST.get('price')
#             order.order = type_order
#             order.condition = condition
#             order.worker = worker
#             order.author = request.user
#             order.save()
#             for f in files:
#                 order_file = Order_file(request.POST, request.FILES)
#                 order_file = Order_file(files=f, order=order)
#                 order_file.save()
#                 return redirect('home_page')
#
#     else:
#         form = ManagerBlankForm()
#     client = Client.objects.all()
#     status = Status.objects.all()
#     condition = Condition.objects.all()
#     worker = Worker.objects.all()
#     type_order = Order.objects.all()
#     context = {'form':form,
#                'client':client,
#                'status':status,
#                'condition':condition,
#                'worker':worker,
#                'type_order':type_order,
#                }
#     return render(request, 'orders/add_order.html', context)


def order_detail(request, pk):
    order = ManagerBlank.objects.filter(id=pk)
    context = {
        'orders': order,
    }
    return render(request, 'orders/order_detail1.html',
                  context)


def worker_detail(request, pk):
    order = ManagerBlank.objects.filter(id=pk)
    context = {
        'orders': order,
    }
    return render(request, 'orders/worker_detail.html',
                  context)


def order_edit(request, pk):
    order = ManagerBlank.objects.filter(id=pk).first()
    if request.user != order.author:
        return redirect('home_page')
    if request.method == 'POST':
        form = ManagerBlankForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения Сохранены')
            return redirect('home_page')
    form = ManagerBlankForm(instance=order)
    context = {
        'order':order,
        'form':form
    }
    return render(request, 'orders/order_edit.html', context)


def worker_edit(request, pk):
    orders = ManagerBlank.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = WorkerEditForm(request.POST, request.FILES, instance=orders)
        if form.is_valid():
            instance = form.save(commit=False)
            if Material.objects.filter(title=instance.wasted_material_one):
                material = Material.objects.filter(title=instance.wasted_material_one)
                for i in material:
                    i.amount -= instance.amount_wasted_material_one
                    i.save()
                instance.save()
            if Material.objects.filter(title=instance.wasted_material_two):
                material = Material.objects.filter(title=instance.wasted_material_two)
                for i in material:
                    i.amount -= instance.amount_wasted_material_two
                    i.save()
                instance.save()
            if Material.objects.filter(title=instance.wasted_material_three):
                material = Material.objects.filter(title=instance.wasted_material_three)
                for i in material:
                    i.amount -= instance.amount_wasted_material_three
                    i.save()
                instance.save()
            if Material.objects.filter(title=instance.wasted_material_four):
                material = Material.objects.filter(title=instance.wasted_material_four)
                for i in material:
                    i.amount -= instance.amount_wasted_material_four
                    i.save()
                instance.save()
            if Material.objects.filter(title=instance.wasted_material_five):
                material = Material.objects.filter(title=instance.wasted_material_five)
                for i in material:
                    i.amount -= instance.amount_wasted_material_five
                    i.save()
                instance.save()
            if Material.objects.filter(title=instance.wasted_material_six):
                material = Material.objects.filter(title=instance.wasted_material_six)
                for i in material:
                    i.amount -= instance.amount_wasted_material_six
                    i.save()
                instance.save()
            if Material.objects.filter(title=instance.wasted_material_seven):
                material = Material.objects.filter(title=instance.wasted_material_seven)
                for i in material:
                    i.amount -= instance.amount_wasted_material_seven
                    i.save()
                instance.save()
            if Material.objects.filter(title=instance.wasted_material_eight):
                material = Material.objects.filter(title=instance.wasted_material_eight)
                for i in material:
                    i.amount -= instance.amount_wasted_material_eight
                    i.save()
                instance.save()
            instance.save()
            messages.success(request, 'Изменения Сохранены')
            return redirect('home_page')
    # if request.user.position != 'Менеджер':
    #     orders.design = True
    #     orders.Worker = 'Менеджер'
    #     orders.save()
    form = WorkerEditForm(instance=orders)
    context = {
            'order': orders,
            'form': form
        }
    return render(request, 'orders/worker_edit.html', context)


# def complete_order(request, pk):
#     orders = ManagerBlank.objects.filter(id=pk).first()
#     if request.user.position != 'Менеджер':
#         orders.design = True
#         orders.worker = 'Менеджер'
#         orders.save()
#         return redirect('/')
#     context = {
#         'orders': orders
#     }
#     return render(request, 'orders/worker_edit.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def search(request):
    query = request.GET.get('q')
    orders = ManagerBlank.objects.filter(title__icontains=query)
    return render(request, 'orders/home.html',
                  context={'orders': orders})


def invoice(request, pk):
    orders = ManagerBlank.objects.filter(id=pk)
    showtime = strftime('%d/%m', gmtime())
    you_date = dateformat.format(datetime.now(), settings.DATE_FORMAT)
    for i in orders:
        price = str(i.price)
        word_price = num2words(price[:-3], lang='ru')

    context = {
        "orders": orders,
        'date': showtime,
        'mont': you_date,
        'price': word_price.capitalize()
    }
    # return render_to_pdf('invoice/invoice.html', context)
    return render(request, 'invoice/invoice.html', context)


