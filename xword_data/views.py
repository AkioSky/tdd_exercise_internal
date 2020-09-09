from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Puzzle, Entry, Clue


# Create your views here.
def drill(request):
    is_error = False
    if request.method == 'POST':
        answer = request.POST.get('answer')
        clue_id = request.POST.get('clue_id')
        clue = Clue.objects.get(pk=clue_id)
        if clue.entry.entry_text == answer.upper():
            messages.success(request, "Congratulation!")
            return redirect('xword:answer', pk=clue.pk)
        is_error = True
    else:
        clue = Clue.objects.order_by('?').first()
    return render(request, 'xword_data/drill_view.html', context={
        'rand_clue': clue,
        'is_error': is_error
    })


def answer(request, pk):
    clue = Clue.objects.get(pk=pk)

    return render(request, 'xword_data/answer_view.html', context={
        'clue': clue,
        'text': 'only appearance of this clue'
    })
