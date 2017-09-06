# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', all_tracks , name='alltracks'),
    url(r'^(?P<pk>\d+)$', QuestionDetail.as_view(template_name='question_detail.html'), name="question-detail"),
    url('^test',test,name="test"),
    url(r'^tracks/(?P<id>\d+)',track,name="track"),
    url('^allquestions/',QuestionList.as_view(template_name='question_list.html'),name="allquestions"),
    url(r"^leaderboard",leaderboard,name="leaderboard")

]
