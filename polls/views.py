from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def detail(request, question_id):
    return HttpResponse(f'You are looking for a question {question_id}')

def results(request, question_id):
    return HttpResponse(f'You are looking for the results of question {question_id}')

def vote(request, question_id):
    return HttpResponse(f'You are voting for question {question_id}')

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    output = '<hr>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(f'{output}')