from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse(f'You are looking for the results of question {question_id}')

def vote(request, question_id):
    return HttpResponse(f'You are voting for question {question_id}')

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)