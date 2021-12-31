from django.contrib import admin
from .models import Question, QuestionTopic


class QuestionTopicAdmin(admin.ModelAdmin):
    list_display = ['topic', 'slug', 'description', 'note']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'topic', 'slug', 'correct_answer', 'short_explanation', 'explanation_source', 'note']


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionTopic, QuestionTopicAdmin)
