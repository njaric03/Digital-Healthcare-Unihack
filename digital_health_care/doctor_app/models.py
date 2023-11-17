from django.db import models

class Specialization(models.Model):
    SPECNAME = models.CharField(max_length=50, verbose_name="Specialization")
    SPECSDESC = models.CharField(max_length=100, verbose_name="Description")

    def __str__(self):
        return self.SPECNAME

class Doctor(models.Model):
    FNAME = models.CharField(max_length=30, verbose_name="First Name")
    LNAME = models.CharField(max_length=30, verbose_name="Last Name")
    Specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.FNAME} {self.LNAME}"

class Patient(models.Model):
    FNAME = models.CharField(max_length=30, verbose_name="First Name")
    LNAME = models.CharField(max_length=30, verbose_name="Last Name")
    CARD_EXPIRY_DATE = models.DateField()
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.FNAME} {self.LNAME}"

class Medication(models.Model):
    MEDNAME = models.CharField(max_length=40, verbose_name="Medication Name")
    QUANTITY = models.IntegerField()

    def __str__(self):
        return self.MEDNAME

class MedForSpec(models.Model):
    Medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    Specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Medication} for {self.Specialization}"

class DocMedPermission(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    MedForSpec = models.ForeignKey(MedForSpec, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Doctor} has permission for {self.Medication} ({self.MedForSpec})"

class Receipt(models.Model):
    USED = models.CharField(max_length=1, default="N", verbose_name="Used")
    EXPIRYDATE = models.DateField(verbose_name="Expiry Date")
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receipt for {self.Patient} by {self.Doctor}"

class ReceiptMedication(models.Model):
    Receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    DocMedPermission = models.ForeignKey(DocMedPermission, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receipt Medication: {self.Receipt} - {self.DocMedPermission}"

class Pharmacy(models.Model):
    PHARNAME = models.CharField(default ='Benu',  max_length = 50)

    def __str__(self):
        return self.PHARNAME

class HasMedication(models.Model):
    Medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    Pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    QUANTITY = models.IntegerField(verbose_name="Quantity")

    def __str__(self):
        return f"{self.Medication} in {self.Pharmacy}"