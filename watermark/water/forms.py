from django import forms

from water.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)
