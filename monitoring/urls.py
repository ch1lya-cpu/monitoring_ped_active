from django.urls import path
from . import views

urlpatterns = [
    # начальные страницы
    path('', views.index, name='index'),
    path('profile/', views.profilePage, name='profile'),
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
    path("event_update/<str:pk>/", views.updateEvent, name='event_update'),
    path("event_delete/<str:pk>/", views.deleteEvent, name='event_delete'),
    path("createEvent/", views.createEvent, name='createEvent'),
    # основной контент (активности)
    path("activity/", views.activityView, name='activity'),
    path("createActivity/", views.createActivity, name='createActivity'),
    path("activity/<str:pk>/", views.activityDetail, name='activity_detail'),
    path("activity_update/<str:pk>/", views.updateActivity, name='activity_update'),
    path("activity_delete/<str:pk>/", views.deleteActivity, name='activity_delete'),
    # основной контент (ПЦК)
    path("pck/", views.pckView, name='pck'),

]
