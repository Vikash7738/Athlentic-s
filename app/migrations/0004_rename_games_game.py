# Generated by Django 4.0.4 on 2022-04-27 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_games'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='games',
            new_name='game',
        ),
    ]