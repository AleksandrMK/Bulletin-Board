from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Ad, Response


class AdForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Ad
        fields = [
            'title',
            'text',
            'category',
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text',
        ]


class ResponseFormUpdate(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'status',
        ]
