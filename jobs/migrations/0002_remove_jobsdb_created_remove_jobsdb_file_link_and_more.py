# Generated by Django 4.1.1 on 2022-10-11 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobsdb',
            name='created',
        ),
        migrations.RemoveField(
            model_name='jobsdb',
            name='file_link',
        ),
        migrations.RemoveField(
            model_name='jobsdb',
            name='gen_JOBID',
        ),
        migrations.RemoveField(
            model_name='jobsdb',
            name='get_id',
        ),
        migrations.RemoveField(
            model_name='jobsdb',
            name='updated',
        ),
    ]