# Generated by Django 4.1.3 on 2022-11-24 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trello_app", "0004_alter_board_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
        migrations.AlterField(
            model_name="board",
            name="title",
            field=models.CharField(max_length=150),
        ),
    ]
