# Generated by Django 3.2.2 on 2021-05-06 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coursedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.IntegerField()),
                ('Coursetitle', models.CharField(max_length=500)),
                ('Coursename', models.CharField(max_length=500)),
                ('Coursesectioncode', models.IntegerField()),
                ('Coursedepartment', models.CharField(max_length=500)),
                ('InstructorName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Studentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.IntegerField()),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('major', models.CharField(max_length=500)),
                ('year', models.CharField(max_length=500)),
                ('GPA', models.IntegerField()),
            ],
        ),
    ]
