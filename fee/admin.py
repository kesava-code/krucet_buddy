from django.contrib import admin
from .models import FeeDetail, FeeType
# Register your models here.
admin.site.register([FeeDetail, FeeType])