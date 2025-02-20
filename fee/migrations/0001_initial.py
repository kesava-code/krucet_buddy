# Generated by Django 4.2.2 on 2023-06-16 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('totalAmount', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duiNo', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('verified', models.BooleanField(default=False)),
                ('feeType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fee.feetype')),
            ],
        ),
    ]
