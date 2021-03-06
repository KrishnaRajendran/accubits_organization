# Generated by Django 4.0.3 on 2022-03-30 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0020_rename_department_name_department_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='organization.department')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.designation')),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emailID', to='organization.employee')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.employee')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='organization.team')),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeDetails',
        ),
    ]
