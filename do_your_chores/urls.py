from django.urls import path 
from .views import ChoreBoard, NewHousehold, HouseholdDetail, NewMember, MemberDetail, NewTask, TaskDetail, DeleteTask, DeleteTask, DeleteMember, DeleteHousehold

app_name = 'chores'
urlpatterns = [
    path('', ChoreBoard.as_view(), name='chores_board'),
    path('house/new', NewHousehold.as_view(), name='new_house'),
    path('house/<int:pk>', HouseholdDetail.as_view(), name='household_detail'),
    path('house/<int:pk>/delete', DeleteHousehold.as_view(), name='delete_household'),
    path('member/new', NewMember.as_view(), name='new_member'),
    path('member/<int:pk>', MemberDetail.as_view(), name='member_detail'),
    path('member/<int:pk>/delete', DeleteMember.as_view(), name='delete_member'),
    path('task/new', NewTask.as_view(), name='new_task'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('task/<int:pk>/delete', DeleteTask.as_view(), name='delete_task'),
    ]
