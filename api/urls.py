from django.urls import path
from .views import CreateTaskView, ListTaskView, ListUsersView


app_name = "api"

urlpatterns = [
    path("", CreateTaskView.as_view(), name="listcreate"),
    path("<int:pk>/", ListTaskView.as_view(), name="listview"),
    path("users/", ListUsersView.as_view(), name="listusers"),
]
