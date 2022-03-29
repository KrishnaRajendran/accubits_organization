# Generated by Django 4.0.3 on 2022-03-29 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_alter_department_department_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='team_name',
        ),
        migrations.RemoveField(
            model_name='designation',
            name='employee_name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='employee_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.designation'),
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ManyToManyField(to='organization.team'),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='designation',
            name='employee_designation',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
