from django.urls import path
from . import views

app_name = "polls"
# https://docs.djangoproject.com/en/4.2/intro/tutorial03/#namespacing-url-names
# это нужно если у нас например 10 или 20 приложении и django нужно их как то различать в {% url %}
# мы можем добавить app_name
# будет работать так {% url "polls:detail" question.id %}
# мы добавили до ":" polls это значение переменной app_value

urlpatterns = [
	path("", views.index, name="index"),
	path("<int:question_id>/detail/", views.detail, name="detail"),
	path("<int:question_id>/results/", views.results, name="results"),
	path("<int:question_id>/vote/", views.vote, name="vote"),
]
