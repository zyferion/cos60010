# Generated by Django 4.0.4 on 2022-05-18 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_subject_remove_enrolment_end_dttm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='end_dttm',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='subject',
            name='start_dttm',
            field=models.DateField(),
        ),
    ]
