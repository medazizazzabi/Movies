# Generated by Django 4.0.2 on 2022-03-22 01:38

from django.db import migrations, models
import movie.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_movie_duration_alter_movie_geners_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='geners',
        ),
        migrations.AddField(
            model_name='movie',
            name='geners',
            field=models.ManyToManyField(blank=True, null=True, to='movie.Genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, default=movie.models.get_default_movie_image, null=True, upload_to=movie.models.get_movie_image_filepath),
        ),
    ]
