from django import forms

from .models import Poll, Choice, Answer


class PoolForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text',]


# class AnswerForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         self.choices = kwargs.pop('choices')
#         super(AnswerForm, self).__init__(*args, **kwargs)
#         self.fields['mt_arg'] =
#     answer = forms.ChoiceField(choices=, required=True,label='Ответ')


