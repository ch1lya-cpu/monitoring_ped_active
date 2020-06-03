from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("", views.EventView.as_view(), name='event_list'),
    path("", views.TeacherView.as_view(), name='teacher_list'),
    path("<str:slug>/", views.TeacherDetailView.as_view(), name='teacher_detail'),

]
