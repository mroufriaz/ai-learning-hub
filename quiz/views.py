import json
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .models import Question

def quiz_view(request):
    # fetch all questions (order by id); you can randomize or limit via queryset
    qs = Question.objects.all().order_by('id')

    # Build list of dicts to match your JS structure:
    questions = []
    for q in qs:
        questions.append({
            "question": q.text,
            "options": q.options,
            "answer": q.correct_index
        })

    questions_json = mark_safe(json.dumps(questions))  # safe because content comes from DB
    return render(request, "quiz/quiz.html", {"questions_json": questions_json})
