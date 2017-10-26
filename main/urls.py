from django.conf.urls import url

from main import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game$', views.game, name='game'),
    url(r'^finished$', views.finished, name='finished'),
    url(r'^set-category$', views.setCategory, name='set_category'),
    url(r'^set-questions$', views.setQuestions, name='set_questions'),
    url(r'^get-question$', views.getQuestion, name='get_question'),
    url(r'^check-answer$', views.checkAnswer, name='check_answer')
]
