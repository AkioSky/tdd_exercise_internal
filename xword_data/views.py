from django.shortcuts import render
from .models import Puzzle, Entry, Clue


# Create your views here.
def drill(request):
    return render(request, 'xword_data/drill_view.html')


def answer(request):
    return render(request, 'xword_data/answer_view.html')
