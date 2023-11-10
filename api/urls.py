from django.urls import path
from .views import CreateTaskView


app_name = 'api'

urlpatterns = [
    path('', CreateTaskView.as_view(), name='listcreate'),
    # path('<int:pk>/', ViewTask.as_view(), name='listview'),
]
