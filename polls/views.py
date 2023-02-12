from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s. Ok now, don't stare at it for too long" % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s. What else did you think is gonna show up here?"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s. Use your rights to vote, don't just slouch away at your couch like I do``````" % question_id)