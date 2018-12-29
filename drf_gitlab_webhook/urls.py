from django.conf.urls import url
from . import classviews

urlpatterns = [
    url(r'^event/$', classviews.HookEvent.as_view()),
]
