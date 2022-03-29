# Generated by Django 4.0.3 on 2022-03-29 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0015_alter_employee_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='team',
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.team'),
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_name',
        ),
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.ManyToManyField(to='organization.department'),
        ),
    ]
