# Generated by Django 5.2.2 on 2025-06-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]
