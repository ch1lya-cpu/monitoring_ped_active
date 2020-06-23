from django.urls import path
from . import views

urlpatterns = [
    # начальные страницы
    path('', views.index, name='index'),
    # Авторизация и регистрация
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registration/', views.registrationPage, name='registration'),
    # основной контент (преподаватели)
    path("teacher/", views.teacherView, name='teacher'),
    path("teacher/<str:pk>/", views.teacherDetail, name='teacher_detail'),
    path("create_teacher/", views.createTeacher, name='create_teacher'),
    path("teacher_update/<str:pk>/", views.updateTeacher, name='teacher_update'),
    path("teacher_delete/<str:pk>/", views.deleteTeacher, name='teacher_delete'),
    # основной контент (события)
    path("event/", views.eventView, name='event'),
    path("event/<str:pk>/", views.eventDetail, name='event_detail'),
    path("create_event/", views.createEvent, name='create_event'),
    path("event_update/<str:pk>/", views.updateEvent, name='event_update'),
    path("event_delete/<str:pk>/", views.deleteEvent, name='event_delete'),
    # основной контент (активности)
    path("activity/", views.activityView, name='activity'),
    path("activity/<str:pk>/", views.activityDetail, name='activity_detail'),
    path("create_activity/", views.createActivity, name='create_activity'),
    path("update_activity/<str:pk>/", views.updateActivity, name='update_activity'),
    path("delete_activity/<str:pk>/", views.deleteActivity, name='delete_activity'),
    # основной контент (ПЦК)
    path("pck/", views.pckView, name='pck'),

]
