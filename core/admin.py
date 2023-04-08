from django.contrib import admin
from .models import Post, Autor, Cargo
# Register your models here.


@admin.register(Post)
class ShowPosts(admin.ModelAdmin):
    list_display = ('title', 'autor', 'theme', 'status', 'creationDt')
    prepopulated_fields = {'title_slug': ('title',)}
    search_fields = ('title', 'theme', 'status')


@admin.register(Autor)
class ShowAutors(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'email', 'cargo')


@admin.register(Cargo)
class ShowCargos(admin.ModelAdmin):
    list_display = ('name', 'description')
