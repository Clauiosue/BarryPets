from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Pet
from .forms import PetForm, SignUpForm

@login_required
def pet_list(request):
    pets = Pet.objects.filter(owner=request.user)
    print("Rendering pet_list.html with pets:", pets)
    return render(request, 'accounts/pet_list.html', {'pets': pets})

@login_required
def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'accounts/pet_detail.html', {'pet': pet})

@login_required
def pet_new(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetForm()
    return render(request, 'accounts/pet_new.html', {'form': form})


@login_required
def pet_edit(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetForm(instance=pet)
    return render(request, 'accounts/pet_edit.html', {'form': form})

@login_required
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.delete()
    return redirect('pet_list')

@login_required
def user_detail(request):
    user = request.user
    return render(request, 'accounts/user_detail.html', {'user': user})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts/index.html')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pet_list')
            else:
                print("User authentication failed.")
        else:
            print("Form is not valid.")
    else:
        form = AuthenticationForm()
    print("Rendering login.html with form:", form)
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def test_view(request):
    return render(request, 'accounts/test.html')


def index(request):
    return render(request, 'accounts/index.html')

def servicios(request):
    return render(request, 'accounts/servicios.html')

def producto(request):
    return render(request, 'accounts/producto.html')

def QuienesSomos(request):
    return render(request, 'accounts/QuienesSomos.html')

def contacto(request):
    return render(request, 'accounts/contacto.html')