# Generated by Django 5.1.5 on 2025-01-31 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_carouselimages_carouselimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiveSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('map_url', models.URLField(max_length=255)),
                ('image', models.ImageField(upload_to='staticfiles/images/sites/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cost', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
    ]
