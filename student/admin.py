from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Student, Caste, SubCaste, Gender, Regulation, Semester, Passout, Branch, Entry, Stay])