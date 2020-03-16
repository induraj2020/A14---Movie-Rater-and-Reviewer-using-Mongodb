from djongo import models
from django import forms


class Rating(models.Model):
    ratingValue = models.IntegerField()

    class Meta:
        abstract = True

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = (
            'ratingValue',
        )

class Genre(models.Model):
    genreType = models.CharField(max_length=200)

    class Meta:
        abstract = True

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = (
            'genreType',
        )

class Actor(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = (
            'name',
        )

class Comment(models.Model):
    commentT = models.TextField()

    class Meta:
        abstract = True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'commentT',
        )

class Movies(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)

    genres = models.ArrayField(
        model_container=Genre,
        model_form_class=GenreForm
    )

    ratings = models.ArrayField(
        model_container=Rating,
        model_form_class=RatingForm
    )

    posterURL = models.CharField(max_length=255)
    storyline = models.TextField()
    imdbRating = models.FloatField()

    actors = models.ArrayField(
        model_container=Actor,
        model_form_class=ActorForm
    )

    comments = models.ArrayField(
        model_container=Comment,
        model_form_class=CommentForm
    )

    def __str__(self):
        return self.title






#
#
#
# from djongo import models
# from django import forms
#
# class Movies(models.Model):
#     title = models.CharField(max_length=200)
#     year = models.CharField(max_length=4)
#
#     genres = models.ListField()
#
#     ratings = models.ListField()
#
#     # ratings = models.ArrayField(
#
#     # )
#
#     posterURL = models.CharField(max_length=255)
#     storyline = models.TextField()
#     imdbRating = models.FloatField()
#
#     actors = models.ListField()
#
#     comments = models.ListField()
#
#     def __str__(self):
#         return self.title














# class Rating(models.Model):
#     ratingValue = models.IntegerField()
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.ratingValue
#
# class Genre(models.Model):
#     genreType = models.CharField(max_length=200)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.genreType
#
# class Actor(models.Model):
#     name = models.CharField(max_length=200)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.name
#
# class Comment(models.Model):
#     commentT = models.TextField()
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.commentT
#
# class Movies(models.Model):
#     title = models.CharField(max_length=200)
#     year = models.CharField(max_length=4)
#
#     genres = models.ArrayField(
#         model_container=Genre
#     )
#
#     ratings = models.ArrayField(
#         model_container=Rating
#     )
#
#     poster = models.CharField(max_length=255)
#     contentRating = models.CharField(max_length=255)
#     duration = models.CharField(max_length=255)
#     releaseDate = models.CharField(max_length=255)
#     averageRating = models.IntegerField(default=0)
#     originalTitle = models.CharField(max_length=255)
#
#     storyline = models.TextField()
#
#     actors = models.ArrayField(
#         model_container=Actor,
#     )
#
#     imdbRating = models.ListField()
#     posterURL = models.CharField(max_length=255)
#
#     comments = models.ArrayField(
#         model_container=Comment,
#     )
#
#     def __str__(self):
#         return self.title