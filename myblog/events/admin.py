from django.contrib import admin
from .models import Event, EventComments, Sport, Participation, EventLikes

class CommentsInline(admin.TabularInline):
    model = EventComments

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location','sports_display')

    @admin.display(description='Виды спорта')
    def sports_display(self, obj):
        return ', '.join([sport.name for sport in obj.sports.all()])

    list_filter = ('date', 'location')
    inlines = [CommentsInline]
    date_hierarchy = 'date'
    search_fields = ('title', 'location')
    list_display_links = ('title', 'location')



@admin.register(EventComments)
class EventsCommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'event')
    list_filter = ('name', 'event')
    raw_id_fields = ('event',)

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    pass

@admin.register(EventLikes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('ip', 'pos')

