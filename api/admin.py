# api/admin.py
from django.contrib import admin
from .models import Hackathon, Submission

@admin.register(Hackathon)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_datetime', 'end_datetime')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'user', 'hackathon', 'is_winner')
    list_filter = ('hackathon',)
    search_fields = ('name', 'user__username', 'hackathon__title')
    actions = ['mark_as_winner']

    def mark_as_winner(self, request, queryset):
        queryset.update(is_winner=True)

    mark_as_winner.short_description = "Mark selected submissions as winners"
