# Generated by Django 4.1.7 on 2023-05-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField()),
                ('adult_no', models.CharField(max_length=50)),
                ('child_no', models.CharField(max_length=50)),
                ('room', models.BooleanField()),
                ('special_request', models.TextField()),
            ],
        ),
    ]