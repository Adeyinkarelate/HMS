# Generated by Django 4.2.2 on 2024-12-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')], default=None, max_length=50, null=True),
        ),
    ]
