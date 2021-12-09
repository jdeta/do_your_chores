from django.shortcuts import render
from django.views.generic.edit import View, CreateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Household, Member, Task

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

class NewTask(CreateView):
    model = Task
    fields = ['name', 'owner']
    success_url = '/house/1' #make this fella dynamic af

class HouseholdDetail(DetailView):
    model = Household

class MemberDetail(DetailView):
    model = Member

class TaskDetail(DetailView):
    model = Task

class DeleteHouse(DeleteView):
    model = Household

class DeleteMember(DeleteView):
    model = Member

class DeleteTask(DeleteView):
    model = Task

