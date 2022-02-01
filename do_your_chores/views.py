from django.shortcuts import render
from django.views.generic.edit import View, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Household, Member, TaskList

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
    model = TaskList
    fields = ['name', 'owner']

    def get_success_url(self):
        back_to_house = self.object.owner.house.pk
        return reverse_lazy('chores:household_detail', args=[back_to_house])
#    success_url = '/house/1' #make this fella dynamic af

class HouseholdDetail(DetailView):
    model = Household

class MemberDetail(DetailView):
    model = Member

class TaskDetail(DetailView):
    model = TaskList

class DeleteHousehold(DeleteView):
    model = Household
    success_url = '/'

class DeleteMember(DeleteView):
    model = Member
    success_url = '/'

class DeleteTask(DeleteView):
    model = TaskList
    success_url = '/'

