# Generated by Django 4.0.4 on 2022-05-18 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_subject_end_dttm_alter_subject_start_dttm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='end_dttm',
            new_name='end_dt',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='start_dttm',
            new_name='start_dt',
        ),
    ]
