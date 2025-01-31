# Generated by Django 5.1.5 on 2025-01-31 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_contact_when_replied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='replied',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='when_replied',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
