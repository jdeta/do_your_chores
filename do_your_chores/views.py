from django.shortcuts import render


def chores_board(request):
    context = {}

    return render(request, 'do_your_chores/chores_board.html', context)
