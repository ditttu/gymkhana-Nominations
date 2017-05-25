from django import forms
from .models import Questionnaire,Question,QUES_TYPES

class BuildForm(forms.Form):
    Title = forms.CharField()
    description = forms.CharField()


class BuildQuestion(forms.Form):

    question_type = forms.CharField(max_length=50,widget=forms.Select(choices=QUES_TYPES))
    question = forms.CharField(max_length=300)
    question_choices = forms.CharField(max_length=512, help_text='add dollar($) symbol between two choices',required=False)
