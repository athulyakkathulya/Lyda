# Generated by Django 4.1.5 on 2023-01-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('orders', '0002_remove_order_order_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Order Accepted', 'Order Accepted'), ('Delivered Successfully', 'Delivered Successfully'), ('Order Cancelled', 'Order Cancelled')], default='Pending', max_length=50),
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
