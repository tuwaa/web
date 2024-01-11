from django.contrib import admin
from .models import Musician,Album,Tag,Category,Article


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)



@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_display = ('first_name', 'last_name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('str','name','release_date',)