from upload.models import Upload
from django.forms import ModelForm


class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['file', 'col_row']
