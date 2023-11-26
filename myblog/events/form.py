from django import forms
from .models import EventComments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = EventComments
        fields = ('name', 'email', 'text_comments')