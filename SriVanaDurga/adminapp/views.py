from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import AddChicksForm, AddMortalityForm, AddFeedForm, AddMedicineForm, AddVaccineForm, AddLiftingForm
from .models import AddChicks, AddMortality, AddFeed, AddMedicine, AddVaccine, AddLifting

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

from django.shortcuts import render, redirect
from .models import AddLifting

def addlifting(request):
    if request.method == 'POST':
        form = AddLiftingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            total_birds = 0
            total_weight = 0
            num_boxes = int(request.POST.get('numBoxes', 0))

            for i in range(1, num_boxes + 1):
                num_birds = request.POST.get(f'boxNumBirds{i}')
                weight = request.POST.get(f'boxWeight{i}')
                print(num_birds,weight)
                if num_birds and weight:
                    total_birds += int(num_birds)
                    total_weight += float(weight)

            instance.total_birds = total_birds
            instance.total_weight = total_weight
            instance.box_count = num_boxes

            instance.save()
            return redirect('addlifting')
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

def viewlifting(request):
    lifting_records = AddLifting.objects.all()
    return render(request, 'viewlifting.html', {'lifting_records': lifting_records})


def box_wise_data(request, id):
    box_wise_records = AddLifting.objects.filter(id=id)
    total_weight = sum(record.total_weight for record in box_wise_records)
    total_birds = sum(record.total_birds for record in box_wise_records)
    box_data = [(record.box_number, record.birds, record.weight) for record in box_wise_records]

    context = {
        'box_wise_records': box_wise_records,
        'total_weight': total_weight,
        'total_birds': total_birds,
        'box_data': box_data,
    }

    return render(request, 'box_wise_data.html', context)
