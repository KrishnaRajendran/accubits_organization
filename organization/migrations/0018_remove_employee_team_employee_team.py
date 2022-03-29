# Generated by Django 4.0.3 on 2022-03-29 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0017_team_department_name_remove_employee_team_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='team',
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.team'),
        ),
    ]