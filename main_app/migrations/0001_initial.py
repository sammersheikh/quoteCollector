# Generated by Django 4.0.2 on 2022-04-14 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('quote', models.CharField(max_length=100)),
                ('by', models.TextField(max_length=250)),
            ],
        ),
    ]