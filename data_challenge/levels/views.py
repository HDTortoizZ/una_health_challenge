from django.shortcuts import render
from django.views.generic import TemplateView


class LevelsView(TemplateView):
    def get(self, request):
        render(request, 'levels/levels_home.html')
