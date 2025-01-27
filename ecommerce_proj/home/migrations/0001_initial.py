# Generated by Django 3.2 on 2025-01-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('otp_expire_at', models.DateTimeField(blank=True, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
