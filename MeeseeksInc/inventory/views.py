from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 
# this is so that you can render the page w/ the context

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # render takes request object as first arg, and template name as second arg, 
    # then a dictionary ('context' in this case) as an optional third arg
    return render(request, 'inventory/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #built-in django function
    return render(request, 'inventory/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)