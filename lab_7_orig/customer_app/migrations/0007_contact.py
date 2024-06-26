# Generated by Django 5.0.1 on 2024-03-17 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0006_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17)),
                ('email', models.EmailField(max_length=254)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_app.customer')),
            ],
        ),
    ]
