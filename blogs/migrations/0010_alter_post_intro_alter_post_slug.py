# Generated by Django 4.0 on 2021-12-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_alter_tag_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
