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
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
