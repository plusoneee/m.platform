# Generated by Django 2.1.5 on 2019-05-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_userslike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userslike',
            old_name='track_id',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='userslike',
            old_name='user_id',
            new_name='track',
        ),
        migrations.AddField(
            model_name='userslike',
            name='user',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]