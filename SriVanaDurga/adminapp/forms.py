from django import forms
from .models import AddChicks, AddMortality, AddFeed, AddMedicine, AddVaccine, AddLifting

class AddChicksForm(forms.ModelForm):
    class Meta:
        model = AddChicks
        fields = '__all__'

class AddMortalityForm(forms.ModelForm):
    class Meta:
        model = AddMortality
        fields = '__all__'

class AddFeedForm(forms.ModelForm):
    class Meta:
        model = AddFeed
        fields = '__all__'

class AddMedicineForm(forms.ModelForm):
    class Meta:
        model = AddMedicine
        fields = '__all__'

class AddVaccineForm(forms.ModelForm):
    class Meta:
        model = AddVaccine
        fields = '__all__'

class AddLiftingForm(forms.ModelForm):
    class Meta:
        model = AddLifting
        fields = '__all__'