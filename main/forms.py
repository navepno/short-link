from .models import Link
from django.forms import ModelForm, TextInput


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['original_link']
        widgets = {
            'original_link': TextInput(),
        }
        labels = {
                'original_link': ''
            }