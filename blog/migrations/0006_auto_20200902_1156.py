# Generated by Django 3.0.8 on 2020-09-02 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200901_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Cover',
            new_name='cover',
        ),
    ]
