# Generated by Django 4.1.4 on 2022-12-17 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_itstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='iStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('hall_ticket', models.CharField(max_length=20)),
                ('branch', models.CharField(choices=[('IT', 'IT'), ('CSE', 'CSE'), ('CS', 'CS'), ('DS', 'DS'), ('ECE', 'ECE'), ('CIV', 'CIV')], default='IT', max_length=10)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='B', max_length=2)),
                ('date_of_birth', models.DateField(default=datetime.date(2022, 12, 17))),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('parent_number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('student_number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('address', models.CharField(max_length=100)),
                ('attendence', models.DecimalField(decimal_places=2, max_digits=5)),
                ('CGPA', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]