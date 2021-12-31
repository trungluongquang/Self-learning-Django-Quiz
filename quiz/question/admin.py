from django.contrib import admin
from .models import Question, QuestionTopic


class QuestionTopicAdmin(admin.ModelAdmin):
    list_display = ['topic', 'slug', 'description', 'note']


admin.site.register(Question)
admin.site.register(QuestionTopic, QuestionTopicAdmin)
