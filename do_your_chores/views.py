from django.shortcuts import render
from django.views.generic.edit import View, CreateView
from django.views.generic.detail import DetailView

from .models import Household, Member

class ChoreBoard(View):

    def get(self, request):
        context = {}
        return render(request, 'do_your_chores/chores_board.html', context)


class NewHousehold(CreateView):
    model = Household
    fields = ['name']
    success_url = '/member/new'


class NewMember(CreateView):
    model = Member
    fields = ['house', 'name']

class HouseholdDetail(DetailView):
    pass

class MemberDetail(DetailView):
    pass
