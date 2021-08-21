# Generated by Django 3.2.6 on 2021-08-17 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('registration_fee_amount', models.IntegerField()),
                ('voting_fee_amount', models.IntegerField()),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Contestants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('ref_number', models.CharField(max_length=200)),
                ('payment_verified', models.BooleanField(default=False)),
                ('last_name', models.CharField(max_length=100)),
                ('other_names', models.CharField(max_length=300)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('photograph', models.ImageField(upload_to='photograph/')),
                ('profession', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('agree_to_terms_and_conditions', models.BooleanField(default=False)),
                ('agree_to_payment_of_registrtion_fee', models.BooleanField(default=False)),
                ('agree_to_provision_of_accurate_information', models.BooleanField(default=False)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contestants', to='contest.contest')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('ref_number', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('contestants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='contest.contestants')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
