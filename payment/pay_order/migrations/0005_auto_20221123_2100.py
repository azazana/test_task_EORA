# Generated by Django 3.2.4 on 2022-11-23 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pay_order', '0004_auto_20221123_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pay_order.tax'),
        ),
    ]
