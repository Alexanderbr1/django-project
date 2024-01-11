from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import Post, Comments, Likes

class CommentsInline(admin.TabularInline):
    model = Comments

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('title', 'author', 'get_formatted_description')
    list_filter = ('author', 'date')
    search_fields = ('title', 'description')
    inlines = [CommentsInline]
    date_hierarchy = 'date'
    list_display_links = ('title', 'author')

    def get_formatted_description(self, obj):
        return obj.description.upper()

    get_formatted_description.short_description = 'Кастомное описание'

    def get_export_queryset(self, request):
        # Например, добавим фильтр по автору
        return super().get_export_queryset(request).filter(author='sport-express')

    def dehydrate_date(self, post):
        # Пример: форматирование даты перед экспортом
        return post.date.strftime("%Y-%m-%d")

    def get_title(self, post):
        # Пример: изменение значения поля "title" перед экспортом
        return f'Custom Title: {post.title}'


@admin.register(Comments)
class CommentsAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('name', 'post')
    list_filter = ('name', 'post')
    raw_id_fields = ('post',)
    list_display_links = ('name', 'post')


@admin.register(Likes)
class LikesAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('ip', 'post')
