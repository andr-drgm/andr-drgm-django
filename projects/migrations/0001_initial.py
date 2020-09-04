# Generated by Django 3.1 on 2020-09-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('slug', models.SlugField(max_length=40)),
                ('tools', models.ManyToManyField(related_name='project', to='projects.Tool')),
            ],
        ),
    ]
