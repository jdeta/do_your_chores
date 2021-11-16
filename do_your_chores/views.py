from django.shortcuts import render
from django.views import View

#def chores_board(request):
#    context = {}

 #   return render(request, 'do_your_chores/chores_board.html', context)

class ChoreBoard(View):

    def get(self, request):
        context = {}
        return render(request, 'do_your_chores/chores_board.html', context)
