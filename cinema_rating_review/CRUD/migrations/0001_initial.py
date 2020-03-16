# Generated by Django 2.2.1 on 2020-03-14 20:02

import CRUD.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
                ('genres', djongo.models.fields.ArrayField(model_container=CRUD.models.Genre, model_form_class=CRUD.models.GenreForm)),
                ('ratings', djongo.models.fields.ArrayField(model_container=CRUD.models.Rating, model_form_class=CRUD.models.RatingForm)),
                ('posterURL', models.CharField(max_length=255)),
                ('storyline', models.TextField()),
                ('imdbRating', models.FloatField()),
                ('actors', djongo.models.fields.ArrayField(model_container=CRUD.models.Actor, model_form_class=CRUD.models.ActorForm)),
                ('comments', djongo.models.fields.ArrayField(model_container=CRUD.models.Comment, model_form_class=CRUD.models.CommentForm)),
            ],
        ),
    ]
