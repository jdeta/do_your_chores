from django.urls import path 
from .views import ChoreBoard

app_name = 'chores'
urlpatterns = [
    path('', ChoreBoard.as_view(), name='chores_board'),
    ]
