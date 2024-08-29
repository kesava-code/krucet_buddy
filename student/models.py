from django.db import models


# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Caste(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class SubCaste(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    caste = models.ForeignKey(
        Caste, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Regulation(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Passout(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    regulation = models.ForeignKey(
        Regulation, on_delete=models.PROTECT, blank=True, null=True)
    status = models.ForeignKey(
        Semester, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Stay(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name

from fee.models import FeeType
class Student(models.Model):
    admissionNo = models.CharField(max_length=15, blank=True, null=True)
    regNo = models.CharField(max_length=50)
    name = models.CharField(max_length=100, blank=True, null=True)
    passout = models.ForeignKey(
        Passout, on_delete=models.PROTECT, blank=True, null=True)

    feeTypes = models.ManyToManyField(FeeType, blank=True, null=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.SET_NULL, blank=True, null=True)
    parentName = models.CharField(max_length=50, blank=True, null=True)
    studentNo = models.CharField(max_length=10, blank=True, null=True)
    parentNo = models.CharField(max_length=10, blank=True, null=True)
    aadhaar = models.CharField(max_length=12, blank=True, null=True)
    gmail = models.EmailField(max_length=254, blank=True, null=True)
    branch = models.ForeignKey(
        Branch, on_delete=models.PROTECT,  blank=True, null=True)
    entry = models.ForeignKey(
        Entry, on_delete=models.PROTECT, blank=True, null=True)
    dateofBirth = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    subCaste = models.ForeignKey(
        SubCaste, on_delete=models.SET_NULL, blank=True, null=True)
    dateofJoining = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    stayType = models.ForeignKey(
        Stay, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.regNo
