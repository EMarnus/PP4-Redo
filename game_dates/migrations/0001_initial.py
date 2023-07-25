# Generated by Django 3.2.20 on 2023-07-25 18:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Online gaming', 'Online Gaming'), ('In person gaming', 'In person gaming'), ('Watch party', 'Watch party'), ('Board games', 'Board games')], default='Online gaming', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('12 AM', '12 AM'), ('1 AM', '1 AM'), ('2 AM', '2 AM'), ('3 AM', '3 AM'), ('4 AM', '4 AM'), ('5 AM', '5 AM'), ('6 AM', '6 AM'), ('7 AM', '7 AM'), ('8 AM', '8 AM'), ('9 AM', '9 AM'), ('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 PM', '12 PM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM'), ('8 PM', '8 PM'), ('9 PM', '9 PM'), ('10 PM', '10 PM'), ('11 PM', '11 PM')], max_length=24)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='game_dates.appointment')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]