from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Teacher, Event, Activity


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
