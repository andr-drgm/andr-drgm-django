# Generated by Django 3.1 on 2020-09-02 09:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200902_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
