from django.shortcuts import render
from django.views.generic import TemplateView
from levels.forms import filter_form_gen


filter_form = filter_form_gen()


class LevelsView(TemplateView):
    def get(self, request):
        form = next(filter_form)
        return render(request, 'levels/levels_home.html', {'form': form})
