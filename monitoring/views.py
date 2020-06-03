from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.base import View

from .models import Teacher, Event


class TeacherView(ListView):
    model = Teacher
    queryset = Teacher.objects.all()
    template_name = 'monitoring/teacher_list.html'


class EventView(ListView):
    model = Event
    queryset = Event.objects.all()
    template_name = 'monitoring/event_list.html'


class TeacherDetailView(DetailView):
    model = Teacher
    slug_field = "url"


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_teachers = Teacher.objects.all().count()
    num_events = Event.objects.all().count()
    # Доступные книги (статус = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    #num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'monitoring/index.html',
        context={'num_teachers': num_teachers, 'num_events': num_events},
    )
