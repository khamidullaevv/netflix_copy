from django.db import models
from django.contrib.auth.models import User
from utils import format_duration


class MovieCategory(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)


def __str__(self):
    return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        MovieCategory, on_delete=models.SET_NULL, null=True, related_name="movies"
    )
    video = models.CharField(max_length=255, blank=True, null=True)
    video_format = models.CharField(max_length=50, blank=True, null=True)
    length_seconds = models.PositiveIntegerField(default=0)


@property
def duration(self):
    return format_duration(self.length_seconds)


def __str__(self):
    return self.name


class MovieTrailer(models.Model):
    ame = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="trailers")
    video = models.CharField(max_length=255)
    length_seconds = models.PositiveIntegerField(default=0)


@property
def duration(self):
    return format_duration(self.length_seconds)


def __str__(self):
    return self.name


class MoviePart(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="parts")
    video = models.CharField(max_length=255)
    length_seconds = models.PositiveIntegerField(default=0)


@property
def duration(self):
    return format_duration(self.length_seconds)


def __str__(self):
    return self.name


class Cast(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="casts")


def __str__(self):
    return f"{self.firstname} {self.lastname}"


class MovieRating(models.Model):
    rating = models.FloatField()
    comments = models.TextField(blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")


class Recommended(models.Model):
    movie_category = models.ForeignKey(
        MovieCategory, on_delete=models.CASCADE, related_name="recommended"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recommended")


class UserLastMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="last_movies")
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="last_users"
    )
