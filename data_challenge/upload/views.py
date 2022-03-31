from django.shortcuts import render
from django.views.generic import TemplateView
from upload.forms import UploadForm


class UploadView(TemplateView):
    """
    This view will allow users to upload files.
    """
    def get(self, request):
        form = UploadForm()
        return render(request, 'upload/upload.html', {'form': form})

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return render(request, 'upload/upload.html', {'form': UploadForm()})

