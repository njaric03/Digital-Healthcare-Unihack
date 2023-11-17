from django.db import models

class Specialization(models.Model):
    SPECNAME = models.CharField(max_length=50)
    SPECSDESC = models.CharField(max_length=100)

class Doctor(models.Model):
    FNAME = models.CharField(max_length=30)
    LNAME = models.CharField(max_length=30)
    Specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

class Patient(models.Model):
    FNAME = models.CharField(max_length=30)
    LNAME = models.CharField(max_length=30)
    CARD_EXPIRY_DATE = models.DateField()
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Medication(models.Model):
    MEDNAME = models.CharField(max_length=40)
    QUANTITY = models.IntegerField()

class MedForSpec(models.Model):
    Medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    Specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

class DocMedPermission(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    MedForSpec = models.ForeignKey(MedForSpec, on_delete=models.CASCADE)

class Receipt(models.Model):
    USED = models.CharField(max_length=1)
    EXPIRYDATE = models.DateField()
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class ReceiptMedication(models.Model):
    Receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    DocMedPermission = models.ForeignKey(DocMedPermission, on_delete=models.CASCADE)

class Pharmacy(models.Model):
    PHARNAME = models.CharField(max_length = 50)

class HasMedication(models.Model):
    Medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    Pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    QUANTITY = models.IntegerField()