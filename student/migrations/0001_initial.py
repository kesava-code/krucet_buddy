# Generated by Django 4.2.2 on 2023-06-17 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Caste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('caste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.caste')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionNo', models.CharField(blank=True, max_length=15, null=True)),
                ('regNo', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('parentName', models.CharField(blank=True, max_length=50, null=True)),
                ('studentNo', models.CharField(blank=True, max_length=10, null=True)),
                ('parentNo', models.CharField(blank=True, max_length=10, null=True)),
                ('aadhaar', models.CharField(blank=True, max_length=12, null=True)),
                ('gmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('dateofBirth', models.DateField(blank=True, null=True)),
                ('dateofJoining', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=254, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='student.branch')),
                ('entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='student.entry')),
                ('feeTypes', models.ManyToManyField(blank=True, null=True, to='fee.feetype')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.gender')),
                ('passout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='student.passout')),
                ('stayType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.stay')),
                ('subCaste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.subcaste')),
            ],
        ),
        migrations.AddField(
            model_name='passout',
            name='regulation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='student.regulation'),
        ),
        migrations.AddField(
            model_name='passout',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='student.semester'),
        ),
    ]
