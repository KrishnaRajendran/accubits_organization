# Generated by Django 4.0.3 on 2022-03-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0011_alter_department_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=100),
        ),
    ]
