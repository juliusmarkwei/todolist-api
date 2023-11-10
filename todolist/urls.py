from django.views.generic import TemplateView
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', TemplateView.as_view(template_name='todolist/index.html'))
]
