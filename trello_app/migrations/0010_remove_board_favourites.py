# Generated by Django 4.1.3 on 2022-11-23 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trello_app", "0009_alter_board_favourites"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="board",
            name="favourites",
        ),
    ]
