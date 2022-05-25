# Generated by Django 4.0.4 on 2022-05-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuids', models.IntegerField()),
                ('stuname', models.CharField(max_length=70)),
                ('stuemail', models.EmailField(max_length=70)),
                ('stupass', models.CharField(max_length=70)),
            ],
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='user',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='UserMembership',
        ),
    ]
