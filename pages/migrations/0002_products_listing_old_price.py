# Generated by Django 5.0.4 on 2024-04-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_listing',
            name='old_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]