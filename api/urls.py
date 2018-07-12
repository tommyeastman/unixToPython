from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('countlines/', views.countlines, name='countlines'),
    path('getcwd/', views.getcwd, name='getcwd'),
    path('generateNewPredictions/', views.generate_new_predictions,
         name='generateNewPredictions'),
    path('generatePredictionsString/', views.generate_predictions_string,
         name='generatePredictionsString'),
    path('fastText/', views.fasttext, name='fasttext'),
]
