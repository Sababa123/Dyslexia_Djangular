from django import forms
from .models import Question




class Question_classCreateForm(forms.ModelForm):

   
    class Meta:
        model = Question
        fields = [
            'ques',
            'ans1',
            'ans2'
        ]
