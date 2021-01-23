from django import forms

from webapp.models import Messages


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message_text']
