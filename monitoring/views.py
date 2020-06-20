from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages

from django.views.generic import ListView
from django.core.paginator import Paginator

from .forms import TeacherForm
from .models import *
from .decorators import unauthenticated_user


def listing(request):
    teachers = Teacher.objects.all()

    paginator = Paginator(teachers, 2)  # 3 поста на каждой странице

    page = paginator.get_page(1)

    return render(request, 'monitoring/teacher_list.html', {'teachers': page.object_list})


@login_required(login_url='login')
def teacherView(request):
    teachers = Teacher.objects.filter(role='Преподаватель')
    total_teacher = teachers.count()

    activity = Activity.objects.all()

    context = {'teacher': teachers, 'total_teacher': total_teacher, 'activity': activity}

    return render(request, 'monitoring/teacher_list.html', context)


@login_required(login_url='login')
def eventView(request):
    events = Event.objects.all()
    total_event = events.count()

    context = {'event': events, 'total_event': total_event}

    return render(request, 'monitoring/event_list.html', context)


@login_required(login_url='login')
def teacherDetail(request, pk):
    teacher = Teacher.objects.get(id=pk)
    activitys = teacher.activity_set.all()
    activity_count = activitys.count()
    pcks = teacher.teachers_in_pck_set.get(teachers_id=teacher.id)
    qualifics = teacher.qualific_course_for_teachers_set.all()
    qualific_count = qualifics.count()

    Event.objects.filter(activity__teachers_id=teacher)

    context = {'teacher': teacher, 'activitys': activitys,
               'activity_count': activity_count, 'pck': pcks,
               'qualifics': qualifics, 'qualific_count': qualific_count}
    return render(request, 'monitoring/teacher_detail.html', context)


# @login_required(login_url='login')
# def eventDetail(request, pk):
# event = Event.objects.get(activity.teachers.id=)
# events = event.activity_set.all()
# teacher_in_active =
# context = {'event': event}
# return render(request, 'monitoring/event_detail.html', context)


@login_required(login_url='login')
def index(request):
    num_teachers = Teacher.objects.all().count()

    num_events = Event.objects.all().count()

    return render(request, 'monitoring/index.html', context={'num_teachers': num_teachers, 'num_events': num_events})


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Неправильный логин или пароль.')

    context = {}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profilePage(request):
    events = Activity.objects.filter(teachers = request.user)

    #  total_events = events_profile.count()

    #  print('EVENTS:', events_profile)

    context = {"events": events}
    return render(request, 'monitoring/profile.html', context)


@login_required(login_url='login')
def createTeacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save()
            return redirect('/teacher')

    context = {'form': form}
    return render(request, 'monitoring/teacher_form.html', context)


@login_required(login_url='login')
def updateTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect('/teacher/' + pk)

    context = {'form': form}
    return render(request, 'monitoring/teacher_form.html', context)


@login_required(login_url='login')
def deleteTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect('/teacher')

    context = {'item': teacher}
    return render(request, 'monitoring/delete.html', context)


@login_required(login_url='login')
def registrationPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Преподаватель')
            user.groups.add(group)
            # Added username after video because of error returning customer name if not added
            return redirect('/create_teacher')
    context = {'form': form}
    return render(request, 'account/registration.html', context)
