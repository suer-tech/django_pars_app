# Generated by Django 5.0 on 2023-12-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='change_percent',
            field=models.CharField(max_length=20),
        ),
    ]
