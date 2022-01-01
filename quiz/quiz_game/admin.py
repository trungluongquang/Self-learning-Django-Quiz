from django.contrib import admin
from .models import QuizGame, FeaturedQuizGame
from django import forms


class QuizGameForm(forms.ModelForm):
    def clean(self):
        tmp = list()
        i = 1
        while f'slug_question_{i}' in self.cleaned_data:
            key = f'slug_question_{i}'
            if str(self.cleaned_data[key]) in tmp \
                    and self.cleaned_data[key] is not None:
                raise forms.ValidationError({key: 'Duplicate question'})
            tmp.append(str(self.cleaned_data[key]))
            if (self.cleaned_data[key] is None) and (f'slug_question_{i + 1}' in self.cleaned_data):
                if self.cleaned_data[f'slug_question_{i + 1}'] is not None:
                    raise forms.ValidationError({key: 'No empty question inbetween'})
            i += 1


class QuizGameAdmin(admin.ModelAdmin):
    form = QuizGameForm
    search_fields = ['title', 'description', 'slug_question_1', 'slug_question_2', 'slug_question_3', 'slug_question_4',
                     'slug_question_5', 'slug_question_6', 'slug_question_7', 'slug_question_8', 'slug_question_9',
                     'slug_question_10']
    list_display = ['title', 'number_of_questions', 'slug', 'description', 'short_description',
                    'slug_question_1', 'slug_question_2', 'slug_question_3', 'slug_question_4', 'slug_question_5',
                    'slug_question_6', 'slug_question_7', 'slug_question_8', 'slug_question_9', 'slug_question_10']


class FeaturedQuizGameAdmin(admin.ModelAdmin):
    list_display = ['quiz_game_slug']


admin.site.register(QuizGame, QuizGameAdmin)
admin.site.register(FeaturedQuizGame, FeaturedQuizGameAdmin)
