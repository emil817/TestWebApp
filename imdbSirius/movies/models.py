from django.db import models

# Create your models here.

class OriginalName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

class Duration(models.Model):
    name = models.IntegerField()
    def __str__(self) -> str:
        return str(self.name)

class Movie (models.Model):
    name = models.CharField(max_length=64)
    original_name = models.OneToOneField(
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
    duration = models.OneToOneField(
        Duration,
        related_name='movie',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )