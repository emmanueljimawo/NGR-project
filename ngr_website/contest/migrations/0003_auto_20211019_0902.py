# Generated by Django 3.2.6 on 2021-10-19 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_remove_contestant_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be 11 digits and entered in the format: '080**'.", regex='^0\\d{10}$')]),
        ),
    ]