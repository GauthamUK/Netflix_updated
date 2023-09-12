# Generated by Django 4.2.4 on 2023-09-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('action', 'Action'), ('Horror', 'Horror'), ('comedy', 'Comedy'), ('sciencefiction', 'Science fiction'), ('drama', 'Drama'), ('fantasy', 'Fantasy'), ('romance', 'Romance'), ('thriller', 'Thriller'), ('animation', 'Animation'), ('war', 'War')], default='action', max_length=100),
        ),
    ]
