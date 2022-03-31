from django.urls import path
from levels.views import LevelsView


urlpatterns = [
    path('', LevelsView.as_view(), name='levels_home')
]
