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
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    customer_code = models.CharField(max_length=50)
    farm_code = models.CharField(max_length=50)
    vehicle_no = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    num_birds = models.IntegerField()
    num_cages = models.IntegerField()

    class Meta:
        db_table = 'addlifting_table'