from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import *
from .models import *
from .decorators import unauthenticated_user


@login_required(login_url='login')
def teacherView(request):
    teachers = Teacher.objects.filter(role='Преподаватель')

    context = {'teacher': teachers}
    return render(request, 'monitoring/teacher_list.html', context)


@login_required(login_url='login')
def pckView(request):
    pck_teacher = PCK.objects.all()
    total_pck_teacher = pck_teacher.count()

    context = {'pck_teacher': pck_teacher, 'total_pck_teacher': total_pck_teacher}

    return render(request, 'monitoring/pck_list.html', context)


@login_required(login_url='login')
def teacherDetail(request, pk):
    teacher = Teacher.objects.get(id=pk)
    activitys = teacher.activity_set.all()
    activity_count = activitys.count()
    qualifics = teacher.qualific_course_for_teachers_set.all()
    qualific_count = qualifics.count()

    Event.objects.filter(activity__teachers_id=teacher)

    context = {'teacher': teacher, 'activitys': activitys,
               'activity_count': activity_count,
               'qualifics': qualifics, 'qualific_count': qualific_count}
    return render(request, 'monitoring/teacher_detail.html', context)


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
            return redirect('index')
        else:
            messages.info(request, 'Неправильный логин или пароль.')

    context = {}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


################### ПРЕПОДАВАТЕЛИ ###############################################
@login_required(login_url='login')
def registrationPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='Преподаватель')
            user.groups.add(group)
            return redirect('/create_teacher')
    context = {'form': form}
    return render(request, 'account/registration.html', context)


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
    return render(request, 'monitoring/delete_teacher.html', context)


################### СОБЫТИЯ ###############################################
@login_required(login_url='login')
def eventView(request):
    events = Event.objects.all()
    total_event = events.count()

    context = {'event': events, 'total_event': total_event}

    return render(request, 'monitoring/event_list.html', context)


@login_required(login_url='login')
def eventDetail(request, pk):
    event_detail = Event.objects.get(id=pk)
    activity = event_detail.activity_set.all()
    tags = Tag.objects.all()

    context = {'event': event_detail, 'activity': activity, 'tag': tags}
    return render(request, 'monitoring/event_detail.html', context)


@login_required(login_url='login')
def createEvent(request):
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            if 'document_for_event' in request.FILES:
                form.document_for_event = request.FILES['document_for_event']
            form.save()
            return redirect('/event')

    context = {'form': form}
    return render(request, 'monitoring/event_form.html', context)


@login_required(login_url='login')
def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form_event = EventForm(instance=event)

    if request.method == 'POST':
        form_event = EventForm(request.POST, instance=event)

        if form_event.is_valid():
            form_event.save()
            return redirect('/event/' + pk)

    context = {'form': form_event}
    return render(request, 'monitoring/event_form.html', context)


@login_required(login_url='login')
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect('/event')

    context = {'item': event}
    return render(request, 'monitoring/delete_event.html', context)


################### АКТИВНОСТИ ###############################################
@login_required(login_url='login')
def activityView(request):
    activite = Activity.objects.all()

    context = {'activity': activite}

    return render(request, 'monitoring/activity_list.html', context)


@login_required(login_url='login')
def activityDetail(request, pk):
    activity = Activity.objects.get(id=pk)

    context = {'activity': activity, }
    return render(request, 'monitoring/activity_detail.html', context)


@login_required(login_url='login')
def createActivity(request):
    form_activity = ActivityForm(request.POST)

    if request.method == 'POST':
        form_activity = ActivityForm(request.POST)
    if form_activity.is_valid():
        form_activity.save()
        return redirect('/activity')

    context = {'form': form_activity}
    return render(request, 'monitoring/activity_form.html', context)


@login_required(login_url='login')
def updateActivity(request, pk):
    activity = Activity.objects.get(id=pk)
    form_activity = ActivityForm(instance=activity)

    if request.method == 'POST':
        form_activity = ActivityForm(request.POST, instance=activity)

        if form_activity.is_valid():
            form_activity.save()
            return redirect('/activity/' + pk)

    context = {'form': form_activity}
    return render(request, 'monitoring/activity_form.html', context)


@login_required(login_url='login')
def deleteActivity(request, pk):
    activity = Activity.objects.get(id=pk)
    if request.method == "POST":
        activity.delete()
        return redirect('/activity')

    context = {'item': activity}
    return render(request, 'monitoring/delete_event.html', context)
