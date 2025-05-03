from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import path
from django.db.models import Count
from .models import Entry, Vote

# Register your models here.
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'created_by', 'vote_count')
    list_filter = ('created_at', 'created_by')
    search_fields = ('text',)

    def get_vote_count(self, obj):
        return obj.vote_count
    
    get_vote_count.short_description = 'Votes'

    def get_queryset(self, request):
        queryset =  super().get_queryset(request)
        queryset = queryset.annotate(
            votes_count = Count('votes')
        )
        return queryset

    def changelist_view(self, request, extra_context = None):
        total_votes = Vote.objects.count()
        extra_context = extra_context or {}
        extra_context['total_votes'] = total_votes
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('entry', 'created_at', 'session_id')
    list_filter = ('created_at',)

