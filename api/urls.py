from django.urls import path
from .views import CreateTask, ViewTask


app_name = 'api'

urlpatterns = [
    path('', CreateTask.as_view(), name='listcreate'),
    path('<int:pk>/', ViewTask.as_view(), name='listview'),
]
