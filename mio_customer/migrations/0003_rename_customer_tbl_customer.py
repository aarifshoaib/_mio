# Generated by Django 5.1.5 on 2025-01-20 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mio_customer', '0002_customer_delete_tbl_customer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='tbl_customer',
        ),
    ]
