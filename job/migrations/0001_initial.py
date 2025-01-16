# Generated by Django 5.1.5 on 2025-01-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')], max_length=50)),
                ('status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]