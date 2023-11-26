from django.contrib import admin
from .models import Post, Comments, Likes

class CommentsInline(admin.TabularInline):
    model = Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_formatted_description')
    list_filter = ('author', 'date')
    search_fields = ('title', 'description')
    inlines = [CommentsInline]
    date_hierarchy = 'date'
    list_display_links = ('title', 'author')

    def get_formatted_description(self, obj):
        # Ваш собственный код для форматирования описания записи
        return obj.description.upper()

    get_formatted_description.short_description = 'Кастомное описание'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
    list_filter = ('name', 'post')
    raw_id_fields = ('post',)
    list_display_links = ('name', 'post')


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('ip', 'post')
