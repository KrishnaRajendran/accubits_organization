# Generated by Django 4.0.3 on 2022-03-29 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_alter_designation_employee_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.department'),
        ),
    ]
