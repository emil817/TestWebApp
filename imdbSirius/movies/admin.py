from django.contrib import admin

# Register your models here.
from .models import Movie, OriginalName, Duration, Director, Type

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'original_name')
    list_editable = ('name',)

@admin.register(OriginalName)
class OriginalNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Type)
class OriginalNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Director)
class OriginalNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Duration)
class OriginalNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')