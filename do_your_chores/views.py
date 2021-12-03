from django.shortcuts import render
from django.views import View

class ChoreBoard(View):

    def get(self, request):
        context = {}
        return render(request, 'do_your_chores/chores_board.html', context)

class NewMember(View):

    def get(self, request):
        context = {}
        return render(request, 'do_your_chores/new_member.html', context)


class NewChore(View):

    def get(self, request):
        context = {}
        return render(request, 'do_your_chores/new_chore.html', context)
