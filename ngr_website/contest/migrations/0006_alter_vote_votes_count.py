# Generated by Django 3.2.6 on 2021-12-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_auto_20211219_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='votes_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
