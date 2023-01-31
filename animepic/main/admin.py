from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'anime', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('^name', 'content', '^anime')
    list_editable = ('is_published',)
    list_filter = ('time_create', 'is_published')
    prepopulated_fields = {"slug": ("name",)}
    fields = ('name', 'anime', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create')
    readonly_fields = ('time_create', 'get_html_photo')
    list_per_page = 13
    # save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "photo"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Character, CharacterAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Anime Characters"
admin.site.site_header = 'Admins of AnimEpic'