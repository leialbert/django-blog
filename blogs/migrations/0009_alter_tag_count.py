# Generated by Django 4.0 on 2021-12-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_tag_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
