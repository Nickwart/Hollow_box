# Generated by Django 4.0 on 2022-02-17 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopuser',
            options={'permissions': (('admin', 'admin'), ('staff', 'staff'), ('default_user', 'default user'))},
        ),
    ]
