from django.db import models

# Create your models here.

class OriginalName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

class Duration(models.Model):
    name = models.IntegerField(max_length=10)

class Movie (models.Model):
    name = models.CharField(max_length=64)
    originalName = models.OneToOneField(
        OriginalName,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='movie'
    )
    type_id = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name='movie'
    )
    director = models.ManyToManyField(
        Director,
        related_name='movie'
    )
    duration = models.ManyToManyField(
        Duration,
        related_name='movie'
    )