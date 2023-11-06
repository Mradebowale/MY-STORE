from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['Headline', 'Content', 'Reporter', 'images', 'date_reported']