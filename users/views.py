from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm, AddClientForm, ProfileUpdateForm, SearchClientForm
from users.models import Account, Client


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = AddClientForm()
    context = {
        'form': form
    }
    return render(request, 'users/add_client.html', context)


def list_clients(request):
    clients = Client.objects.all()
    form = SearchClientForm(request.POST or None)

    if request.method == 'POST':
        clients = Client.objects.filter(
            first_name__icontains=form['category'].value(),
            last_name__icontains=form['title'].value(),
            organization__icontains=form['organization'].value(),
            phone__icontains=form['color'].value(),
            status__icontains=form['shade'].value()
        )

    context = {
        'clients': clients,
        'form': form
    }
    return render(request, 'users/clients.html', context)


def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    form = ProfileUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)


def client_detail(request, pk):
    client = Client.objects.filter(id=pk)
    context = {
        'clients': client,
    }
    return render(request, 'users/client_detail.html',
                  context)


def client_edit(request, pk):
    client = Client.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = AddClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = AddClientForm(instance=client)
    context = {
        'clients': client,
        'form': form
    }
    return render(request, 'users/client_edit.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            logout(request)
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })

