from django.urls import path
from .views import CreateTaskView, ListTaskView


app_name = 'api'

urlpatterns = [
    path('', CreateTaskView.as_view(), name='listcreate'),
    path('<int:pk>/', ListTaskView.as_view(), name='listview'),
    # path('users/', ListUsers.as_view(), name='listusers'),
]
