# Generated by Django 3.0.2 on 2021-08-14 16:58

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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='img/avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', 'contact'],
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concluded', models.BooleanField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_deals', to='spaces.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_proposal', models.BigIntegerField(null=True)),
                ('deposit_proposal', models.BigIntegerField(null=True)),
                ('kind_desire', models.CharField(default=None, max_length=50, null=True)),
                ('rooms_number_desire', models.IntegerField(default=None, null=True)),
                ('area_desire', models.CharField(default=None, max_length=50, null=True)),
                ('township_desire', models.CharField(default=None, max_length=50, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='spaces.Client')),
            ],
            options={
                'ordering': ['client', 'rent_proposal', 'deposit_proposal'],
            },
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='img/avatars/')),
                ('clients', models.ManyToManyField(related_name='landlords', through='spaces.Deal', to='spaces.Client')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='landlord', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', 'contact'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_township', models.CharField(max_length=50)),
                ('house_area', models.CharField(max_length=50)),
                ('house_rent', models.IntegerField()),
                ('house_deposit', models.IntegerField()),
                ('house_kind', models.CharField(max_length=50)),
                ('house_rooms_number', models.IntegerField()),
                ('house_available', models.BooleanField()),
                ('house_to_sell', models.BooleanField()),
                ('house_image', models.ImageField(upload_to='img/houses/')),
                ('house_creation_day', models.DateTimeField(default=datetime.datetime.now)),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='spaces.Landlord')),
            ],
            options={
                'ordering': ['house_township', 'house_area', 'house_kind', 'house_rooms_number', 'house_rent', 'house_deposit'],
            },
        ),
        migrations.AddField(
            model_name='deal',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landlord_deals', to='spaces.Landlord'),
        ),
    ]
