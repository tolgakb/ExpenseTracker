# Generated by Django 4.2.1 on 2023-05-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]