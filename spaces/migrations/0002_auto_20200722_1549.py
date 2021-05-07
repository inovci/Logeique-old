# Generated by Django 3.0.3 on 2020-07-22 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['house_area', 'house_kind', 'house_rooms_number', 'house_rent', 'house_deposit']},
        ),
        migrations.RenameField(
            model_name='house',
            old_name='area',
            new_name='house_area',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='available',
            new_name='house_available',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='deposit',
            new_name='house_deposit',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='kind',
            new_name='house_kind',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='rent',
            new_name='house_rent',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='rooms_number',
            new_name='house_rooms_number',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='to_sell',
            new_name='house_to_sell',
        ),
        migrations.AddField(
            model_name='house',
            name='house_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='houses/'),
            preserve_default=False,
        ),
    ]
