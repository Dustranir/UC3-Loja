# Generated by Django 5.2.2 on 2025-06-13 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_produto_data_fabricacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data_fabricacao',
            field=models.DateField(default=datetime.datetime(2025, 6, 13, 17, 1, 59, 469691, tzinfo=datetime.timezone.utc)),
        ),
    ]
