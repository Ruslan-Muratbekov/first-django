from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question


# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	template = loader.get_template("polls/index.html")
	# Контекст — это словарь, сопоставляющий имена переменных шаблона с объектами Python.
	context = {
		"latest_question_list": latest_question_list,
	}
	# return render(request, 'polls/index.html', context) - results одинаковый
	return HttpResponse(template.render(context, request))


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	response = "You're voting on question %s."
	return HttpResponse(response % question_id)
