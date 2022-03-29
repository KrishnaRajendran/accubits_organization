# Generated by Django 4.0.3 on 2022-03-28 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_rename_name_designation_employee_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='team_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='designation',
            name='employee_designation',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
