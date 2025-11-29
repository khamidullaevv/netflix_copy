from django.contrib import admin
from .models import (
    Movie,
    MovieCategory,
    MovieTrailer,
    MoviePart,
    Cast,
    MovieRating,
    Recommended,
    UserLastMovie,
)

admin.site.register(Movie)
admin.site.register(MovieCategory)
admin.site.register(MovieTrailer)
admin.site.register(MoviePart)
admin.site.register(Cast)
admin.site.register(MovieRating)
admin.site.register(Recommended)
admin.site.register(UserLastMovie)
