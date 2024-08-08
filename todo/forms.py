from django import forms
from django.core.exceptions import ValidationError

class TodoForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=True,
        error_messages={
            'required': 'タイトルを入力してください。また、スペースのみでは作成できません。'
        }
    )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or title.strip() == "":
            raise ValidationError('タイトルを入力してください。また、スペースのみでは作成できません。')
        return title


class TodoEditForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=False,
        error_messages={
            'required': 'タイトルを入力してください。また、スペースのみでは作成できません。'
        }
    )
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or title.strip() == "":
            raise ValidationError('タイトルを入力してください。また、スペースのみでは作成できません。')
        return title
