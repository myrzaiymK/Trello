# Generated by Django 4.1.3 on 2022-11-20 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
