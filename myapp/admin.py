from django.contrib import admin
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'lowest_note', 'highest_note')
    search_fields = ('title', 'artist')
    ordering = ('title',)
