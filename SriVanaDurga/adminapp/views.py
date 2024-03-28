from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import AddChicksForm, AddMortalityForm, AddFeedForm, AddMedicineForm, AddVaccineForm, AddLiftingForm
from .models import AddChicks, AddMortality, AddFeed, AddMedicine, AddVaccine

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def checkadminlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            if username == "Admin":
                auth_login(request, user)
                return render(request, "index.html")
            else:
                auth_login(request, user)
                return render(request, "index.html")
        else:
            messages.info(request, "Login failed. Please check your Credentials.")
            return render(request, "login.html")

def addfeed(request):
    if request.method == 'POST':
        form = AddFeedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Feed Added Successfully")
    else:
        form = AddFeedForm()
    return render(request, 'addfeed.html', {'form': form})

def addchicks(request):
    if request.method == 'POST':
        form = AddChicksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Chicks Added Successfully")
    else:
        form = AddChicksForm()
    return render(request, 'addchicks.html', {'form': form})

def addmortality(request):
    if request.method == 'POST':
        form = AddMortalityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Mortality Added Successfully")
    else:
        form = AddMortalityForm()
    return render(request, 'addmortality.html', {'form': form})

def addmedicine(request):
    if request.method == 'POST':
        form = AddMedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Medicine Added Successfully")
    else:
        form = AddMedicineForm()
    return render(request, 'addmedicine.html', {'form': form})

def addvaccine(request):
    if request.method == 'POST':
        form = AddVaccineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Vaccine Added Successfully")
    else:
        form = AddVaccineForm()
    return render(request, 'addvaccine.html', {'form': form})

def addlifting(request):
    if request.method == 'POST':
        form = AddLiftingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Lifting Record Added Successfully")
    else:
        form = AddLiftingForm()
    return render(request, 'addlifting.html', {'form': form})

def viewfeed(request):
    feed_records = AddFeed.objects.all()
    return render(request, 'viewfeed.html', {'feed_records': feed_records})

def viewchicks(request):
    chicks_records = AddChicks.objects.all()
    return render(request, 'viewchicks.html', {'chicks_records': chicks_records})

def viewmortality(request):
    mortality_records = AddMortality.objects.all()
    return render(request, 'viewmortality.html', {'mortality_records': mortality_records})

def viewmedicine(request):
    medicine_records = AddMedicine.objects.all()
    vaccine_records = AddVaccine.objects.all()
    return render(request, 'viewmedicine.html', {'medicine_records': medicine_records, 'vaccine_records': vaccine_records})
