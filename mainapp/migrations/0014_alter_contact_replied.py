# Generated by Django 5.1.5 on 2025-01-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_alter_contact_replied_alter_contact_when_replied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='replied',
            field=models.BooleanField(default=False),
        ),
    ]
