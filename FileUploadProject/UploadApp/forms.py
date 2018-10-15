from UploadApp.models import Upload
from django.forms import ModelForm
# FileUpload form class.
class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('name','pic',)
