# Generated by Django 4.0.4 on 2022-05-18 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_end_dttm_subject_end_dt_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Enrolment',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
