from django.urls import path 
from .views import ChoreBoard, NewHousehold, HouseholdDetail, NewMember, MemberDetail 

app_name = 'chores'
urlpatterns = [
    path('', ChoreBoard.as_view(), name='chores_board'),
    path('house/new', NewHousehold.as_view(), name='new_house'),
    path('house/<int:id>', HouseholdDetail.as_view(), name='house_detail'),
    path('member/new', NewMember.as_view(), name='new_member'),
    path('member/<int:id>', MemberDetail.as_view(), name='member_detail'),
    ]
