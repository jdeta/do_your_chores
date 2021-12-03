from django.urls import path 
from .views import ChoreBoard, NewMember, NewChore

app_name = 'chores'
urlpatterns = [
    path('', ChoreBoard.as_view(), name='chores_board'),
    path('member/new', NewMember.as_view(), name='new_member'),
    path('chore/new', NewChore.as_view(), name='new_chore'),
    ]
