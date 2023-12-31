# Generated by Django 5.0 on 2023-12-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('ticker', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_percent', models.CharField(max_length=20)),
            ],
        ),
    ]
