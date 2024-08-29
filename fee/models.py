import datetime
from django.db import models
import datetime
ISO_date = "2021-12-18"
default_date = datetime.date.fromisoformat(ISO_date)

# Create your models here.


class FeeType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    totalAmount = models.CharField(max_length=50,  blank=True, null=True)

    def __str__(self):
        return self.name + " - " + self.totalAmount

from student.models import Student
class FeeDetail(models.Model):
    referenceNumber = models.CharField(max_length=50)
    registerNumber = models.ForeignKey(
        Student, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.CharField(max_length=50)
    feeType = models.ForeignKey(FeeType, on_delete=models.PROTECT)
    verified = models.BooleanField(default=False)
    paymentDate = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True, default=None)

    def __str__(self):
        return self.registerNumber + " - " + self.amount + " - verified: " + str(self.verified)
