from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from levels.forms import filter_form_gen
from upload.models import GlucoseLevels
from datetime import datetime


filter_form = filter_form_gen()


class LevelsView(TemplateView):
    def get(self, request):
        form = next(filter_form)
        return render(request, 'levels/levels_home.html', {'form': form})

    def post(self, request):
        form_class = next(filter_form)
        form = form_class(request.POST)
        timestamp = request.POST["timestamp"].replace(" ", "--")
        sort = request.POST['sort']
        max_rows = request.POST['max_rows']

        if form.is_valid():
            return redirect(f'{request.POST["user_id"]}/{timestamp}/{sort}/{max_rows}')


class FilteredView(TemplateView):
    """
    View for filtered data
    """
    def get(self, request, user_id, timestamp, max_rows, sort):
        """Return generated html based on the objects corresponding to the user_id and timestamp given, the maximum
        number of objects to display and the way the objects should be sorted.

        :param request: user request to server.
        :param user_id: the user id to filter by.
        :param timestamp: the timestamp to filter by.
        :param max_rows: the maximum number of objects to display.
        :param sort: the way the objects should be sorted.
        :return: Generated html from template based on given parameters.
        """
        # get the right format for the parameters.
        max_rows = int(max_rows)
        sort = int(sort)
        timestamp = timestamp.replace('--', ' ')
        timestamp = timestamp[:-6]
        timestamp = datetime.strptime(timestamp, '%Y-%m-%d  %H:%M:%S')
        # load all objects.
        all_models = GlucoseLevels.objects.all()
        # filter objects.
        filtered_models = [item for item in all_models
                           if (str(item.user_id) == user_id and str(item.timestamp) in (str(timestamp) + '+00:00'))]
        # get values ready for the table
        headers = ['User_id', 'Device', 'Serial_number', 'Timestamp', 'Glucose value history', 'Glucose levels']
        records = [(item.user_id,
                    item.device,
                    item.serial_number,
                    item.timestamp,
                    item.glucose_value_history,
                    item.glucose_levels)
                   for item in filtered_models]
        # Sort the objects
        records.sort(key=lambda y: y[sort])
        # Apply length constraint.
        records_length = len(records)
        if records_length > max_rows:
            records = records[:max_rows]

        context = {
            'headers': headers,
            'records': records,
        }
        return render(request, 'levels/filtered.html', context)

