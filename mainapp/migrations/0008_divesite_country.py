# Generated by Django 5.1.5 on 2025-01-31 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='divesite',
            name='country',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
