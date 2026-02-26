from django.forms import ModelForm

from apps.storage.models import FileUpload


class FileUploadForm(ModelForm):
    class Meta:
        fields = ['file']
        model = FileUpload
