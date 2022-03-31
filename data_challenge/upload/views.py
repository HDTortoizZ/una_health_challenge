import os
import pandas
from data_challenge.settings import MEDIA_ROOT
from django.shortcuts import render
from django.views.generic import TemplateView
from upload.forms import UploadForm
from upload.models import GlucoseLevels
from datetime import datetime
import numpy as np


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
            col_row = int(request.POST['col_row'])
            file = request.FILES['file']
            filename = file.name
            df = pandas.read_csv(os.path.join(MEDIA_ROOT, 'uploads', filename),
                                 skiprows=[i for i in range(col_row) if i < col_row - 1]).fillna(0)
            user_id = filename[:-4]
            model_list = list()
            for i in range(df.shape[0]):
                row = df[i:i + 1]
                device = row['Gerät'].item()
                serial_number = row['Seriennummer'].item()
                # Reformat time to datetime field.
                timestamp = datetime.strptime(row['Gerätezeitstempel'].item(), '%d-%m-%Y  %H:%M')
                timestamp = str(timestamp.strftime('%Y-%m-%d %H:%M'))
                glucose_value_history = row['Aufzeichnungstyp'].item()
                glucose_levels = row['Glukosewert-Verlauf mg/dL'].item()
                model = GlucoseLevels(user_id=user_id, device=device, serial_number=serial_number, timestamp=timestamp,
                                      glucose_value_history=glucose_value_history, glucose_levels=glucose_levels)
                model_list.append(model)
            GlucoseLevels.objects.bulk_create(model_list)

        return render(request, 'upload/upload.html', {'form': UploadForm()})

