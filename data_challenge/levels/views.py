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

