# Generated by Django 3.2.10 on 2023-05-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_profile_bklgs_alter_profile_cgpa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placedstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('pck', models.FloatField(default=0)),
            ],
        ),
    ]
