from django.urls import path
from todo import views

urlpatterns = [
    path("addTask/", views.addTask, name="addTask"),
    path("markAsDone/<int:pk>/", views.markAsDone, name="markAsDone"),
    path("markAsUndone/<int:pk>/", views.markAsUndone, name="markAsUndone")
]
