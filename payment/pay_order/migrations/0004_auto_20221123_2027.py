# Generated by Django 3.2.4 on 2022-11-23 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pay_order', '0003_auto_20221123_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='discount',
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pay_order.discount'),
        ),
    ]