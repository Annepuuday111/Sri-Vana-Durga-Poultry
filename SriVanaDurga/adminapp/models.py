from django.db import models

class AddChicks(models.Model):
    title = models.CharField(max_length=100)
    birds = models.IntegerField()
    weeks = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        db_table = 'addchicks_table'

class AddMortality(models.Model):
    date = models.DateField()
    cause_of_death = models.CharField(max_length=50, choices=[
        ('disease', 'Disease'),
        ('accident', 'Accident'),
        ('other', 'Other'),
    ])
    Number_of_Birds = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'addmortality_table'

class AddFeed(models.Model):
    feed_no = models.CharField(max_length=100)
    bags = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        db_table = 'addfeed_table'

class AddMedicine(models.Model):
    date = models.DateField()
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    administration_method = models.CharField(max_length=50, choices=[
        ('oral', 'Oral'),
        ('injection', 'Injection'),
        ('topical', 'Topical'),
    ])
    additional_notes = models.CharField(blank=True)

    class Meta:
        db_table = 'addmedicine_table'

class AddVaccine(models.Model):
    vaccine_name = models.CharField(max_length=100)
    date = models.DateField()
    dose = models.CharField(max_length=50)
    administration_method = models.CharField(max_length=50, choices=[
        ('injection', 'Injection'),
        ('oral', 'Oral'),
        ('spray', 'Spray'),
    ])
    notes = models.CharField(blank=True)

    class Meta:
        db_table = 'addvaccine_table'

class AddLifting(models.Model):
    Date = models.DateField()
    Customer_Name = models.CharField(max_length=100)
    Customer_Code = models.CharField(max_length=50)
    Driver_Name = models.CharField(max_length=100)
    Vehicle_No = models.CharField(max_length=20)
    box_count = models.IntegerField(default=0)
    total_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_birds = models.IntegerField(default=0)
    box_data = models.CharField(max_length=400,default="0_0_0")
    box_number = models.IntegerField(default=0)
    birds = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    class Meta:
        db_table = 'addlifting_table'