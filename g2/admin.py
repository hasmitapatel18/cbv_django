from django.contrib import admin

from .models import *


class FilmAdmin(admin.ModelAdmin):
    fields = [("film_title", "year", "genre", "summary")]


class CommentAdmin(admin.ModelAdmin):
    fields = ["film_comment", "user", "content", "timestamp"]



admin.site.register(Film)
admin.site.register(Comment)
