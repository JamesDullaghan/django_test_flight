from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Format Question Fields in Django Admin"""
    # fields = ['pub_date', 'question_text']
    list_display = ('pub_date', 'question_text', 'was_published_recently')

    fieldsets = [
        (None, {
            'fields': ['question_text']
        }),
        ('Date Information', {
            'fields': ['pub_date'], 'classes': ['collapse']
        }),
    ]
    # Change the way choices display under questions
    # Tabular display with 3 extras
    inlines = [ChoiceInline]
    # Add Date published list filter
    # Because it's a date time field, django gives it some default filter options
    list_filter = ['pub_date']
    # Add search capability
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
