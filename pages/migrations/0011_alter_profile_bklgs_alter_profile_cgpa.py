# Generated by Django 4.0.5 on 2023-04-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_profile_addr_alter_profile_bklgs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bklgs',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cgpa',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
