# Generated by Django 4.0.5 on 2023-05-21 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_placedstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='drives',
            name='drive_cdate',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
