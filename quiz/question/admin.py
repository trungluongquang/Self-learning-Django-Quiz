from django.contrib import admin
from .models import Question, QuestionTopic
from django import forms


class QuestionTopicAdmin(admin.ModelAdmin):
    list_display = ['topic', 'slug', 'description', 'note']


class QuestionForm(forms.ModelForm):
    def clean(self):
        tmp = [str(self.cleaned_data['correct_answer']).lower().strip()]
        for i in range(1, 3):
            key = f'wrong_answer_{i}'
            if str(self.cleaned_data[key]).lower().strip() in tmp:
                raise forms.ValidationError({key: 'Duplicate answer'})
            tmp.append(str(self.cleaned_data[key]).lower().strip())


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    search_fields = ['question', 'note']
    list_display = ['question', 'topic', 'slug', 'correct_answer', 'short_explanation', 'explanation_source', 'note']


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionTopic, QuestionTopicAdmin)
