# Generated by Django 4.2.11 on 2024-05-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
