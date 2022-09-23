# Generated by Django 4.1.1 on 2022-09-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyreport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreportdb',
            name='bsw',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='dailyreportdb',
            name='orifice',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='dailyreportdb',
            name='whp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailyreportdb',
            name='wht',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]