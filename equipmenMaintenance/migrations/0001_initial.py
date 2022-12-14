# Generated by Django 4.1.1 on 2022-09-17 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipmentList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_date_start', models.DateField(null=True)),
                ('ms_type', models.CharField(max_length=20, null=True)),
                ('main_date_end', models.DateField(blank=True, null=True)),
                ('main_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=900, null=True)),
                ('file_link', models.URLField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipmentList.equipment_db')),
            ],
        ),
    ]
