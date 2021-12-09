from django.urls import path 
from .views import ChoreBoard, NewHousehold, HouseholdDetail, NewMember, MemberDetail, NewTask, TaskDetail 

app_name = 'chores'
urlpatterns = [
    path('', ChoreBoard.as_view(), name='chores_board'),
    path('house/new', NewHousehold.as_view(), name='new_house'),
    path('house/<int:pk>', HouseholdDetail.as_view(), name='house_detail'),
    path('member/new', NewMember.as_view(), name='new_member'),
    path('member/<int:pk>', MemberDetail.as_view(), name='member_detail'),
    path('task/new', NewTask.as_view(), name='new_task'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    ]
