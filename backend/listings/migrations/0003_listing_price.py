# Generated by Django 4.0.2 on 2022-02-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
