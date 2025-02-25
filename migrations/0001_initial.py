# Generated by Django 5.1.6 on 2025-02-06 11:59

import django.utils.timezone
import guardian.mixins
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
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('password', models.CharField(blank=True, max_length=128, verbose_name='password')),
                ('anonymous_id', models.CharField(blank=True, max_length=512, null=True, unique=True, verbose_name='Anonymous ID')),
                ('anonymous_id_verified', models.DateTimeField(blank=True, null=True, verbose_name='Anonymous ID verified')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('email_verified', models.DateTimeField(blank=True, null=True, verbose_name='Email verified')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Phone number')),
                ('phone_number_verified', models.DateTimeField(blank=True, null=True, verbose_name='Phone number verified')),
                ('photo_url', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'permissions': (('can_view_quote_materials', 'Can view quote materials'), ('can_view_dashboard', 'Can view dashboard'), ('can_view_custom_page', 'Can view custom page'), ('is_normal_user', 'Is a normal user?')),
            },
            bases=(models.Model, guardian.mixins.GuardianUserMixin),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('provider', models.CharField(max_length=255)),
                ('provider_account_id', models.CharField(max_length=255)),
                ('refresh_token', models.TextField(blank=True, null=True)),
                ('access_token', models.TextField(blank=True, null=True)),
                ('expires_at', models.IntegerField(blank=True, null=True)),
                ('token_type', models.CharField(blank=True, max_length=255, null=True)),
                ('scope', models.CharField(blank=True, max_length=255, null=True)),
                ('id_token', models.TextField(blank=True, null=True)),
                ('session_state', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_token', models.CharField(max_length=255, unique=True)),
                ('expires', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
            },
        ),
        migrations.CreateModel(
            name='VerificationToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255, unique=True)),
                ('expires', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Verification token',
                'verbose_name_plural': 'Verification tokens',
            },
        ),
    ]
