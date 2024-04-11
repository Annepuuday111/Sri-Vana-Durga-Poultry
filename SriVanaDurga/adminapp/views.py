from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
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
            print("num_boxes", num_boxes)
            _boxData = request.POST.get('hiddenTextBox')
            print("box data>>>>", _boxData)


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
            instance.box_data = _boxData
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

    info = AddLifting.objects.filter(id=id).first()
    if info:
        customer_name = info.Customer_Name
        driver_name = info.Driver_Name
        vehicle_no = info.Vehicle_No
    else:
        customer_name = ""
        driver_name = ""
        vehicle_no = ""

    names_table = "<tr><th>Customer Name</th><th>Driver Name</th><th>Vehicle No</th></tr>"
    names_table += "<tr>"
    names_table += f"<td>{customer_name}</td>"
    names_table += f"<td>{driver_name}</td>"
    names_table += f"<td>{vehicle_no}</td></tr>"

    data_table = "<tr><th>Box No</th><th>Birds</th><th>Weight</th></tr>"
    total_birds = 0
    total_weight = 0
    for record in box_wise_records:
        box_data_list = record.box_data.split(",") if record.box_data else []
        for box_data_str in box_data_list:
            box_number, birds, weight = box_data_str.split("_")
            total_birds += int(birds)
            total_weight += int(weight)
            data_table += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(box_number, birds, weight)

    total_row = "<tr>"
    total_row += f"<td>Total Birds:</td><td>{total_birds}</td>"
    total_row += f"<td>Total Weight:</td><td>{total_weight}</td></tr>"

    resHTML = "<div style='padding-left: 100px; padding-right: 100px; text-align: center;'>"
    resHTML += "<br>"
    resHTML += "<h1 style='color: red;'>Box Wise Data</h1>"
    resHTML += "<style>table { width: 100%; border-collapse: collapse; font-size: 30px; } th, td { text-align: center; padding: 8px; border: 2px solid black; }</style>"
    resHTML += "<table><tbody>{}</tbody></table>".format(names_table)
    resHTML += "<br><br>"
    resHTML += "<table><tbody>{}</tbody></table>".format(data_table)
    resHTML += "<br><br>"
    resHTML += "<table><tbody>{}</tbody></table>".format(total_row)
    resHTML += "<br><br>"
    resHTML += "<a href='#' style='font-size: 20px; display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; border-radius: 4px; border: none; cursor: pointer;'>Download PDF</a>".format(id)
    # / download - pdf / {} /
    resHTML += "</div>"

    return HttpResponse(resHTML)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def download_pdf(request, id):
    context = {
        'box_wise_records': AddLifting.objects.filter(id=id),
    }
    pdf = render_to_pdf('pdf_template.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Box_Wise_Data.pdf"
        content = "attachment; filename=%s" % filename
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")



