# Generated by Django 5.0.1 on 2024-03-11 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('director', models.CharField(blank=True, max_length=100, null=True)),
                ('release_year', models.CharField(blank=True, max_length=50, null=True)),
                ('budget', models.CharField(blank=True, max_length=50, null=True)),
                ('runtime', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.CharField(blank=True, max_length=50, null=True)),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=225)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
