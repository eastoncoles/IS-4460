# Generated by Django 5.0.1 on 2024-03-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='emails',
            field=models.CharField(default='a@a.com', max_length=250),
            preserve_default=False,
        ),
    ]