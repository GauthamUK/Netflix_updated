# Generated by Django 4.2.4 on 2023-09-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_backvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backvideo',
            name='vid',
            field=models.URLField(),
        ),
    ]
