# Generated by Django 4.0.1 on 2022-02-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_item_stockcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Description',
            field=models.CharField(max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='InvoiceDate',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='InvoiceDate'),
        ),
        migrations.AlterField(
            model_name='item',
            name='InvoiceNo',
            field=models.CharField(default=0, max_length=135, verbose_name='InvoiceNo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='Quantity',
            field=models.IntegerField(default=0, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='item',
            name='StockCode',
            field=models.CharField(default=0, max_length=135, verbose_name='StockCode'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
