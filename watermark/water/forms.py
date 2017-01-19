from django import forms

from water.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

