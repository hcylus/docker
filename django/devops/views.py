# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template=loader.get_template('devops/index.html')
    context = {
        'question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'devops/index.html', context)


def detail(request, question_id):
    # try:
    # question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('question does not exist')
    # return HttpResponse("you are looking question %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'devops/detail.html', {'question': question})


def results(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'devops/result.html',{'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        raise render(request, 'devops/detail.html',
                     {'question': question, 'error_message': "you don't select choice", })
    else:
        select_choice.vote += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('devops:results', args=(question.id,)))
