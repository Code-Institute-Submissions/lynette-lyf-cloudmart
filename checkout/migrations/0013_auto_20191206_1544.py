# Generated by Django 2.2.7 on 2019-12-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20191206_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Shipping', 'Shipping'), ('Delivered', 'Delivered'), ('Lost', 'Lost')], max_length=50),
        ),
    ]
