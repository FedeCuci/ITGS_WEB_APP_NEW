from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    student = forms.BooleanField(required=False)
    teacher = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'student','teacher', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        teacher = cleaned_data.get('teacher')
        email = cleaned_data.get('email')

        if not student and not teacher:
            raise forms.ValidationError('You must be either a teacher or a studen')
        if email:
            if '@isutrecht.nl' not in email:
                raise forms.ValidationError('You must be a member of ISU to sign up.')
        if email and student:
            if 'student' not in email:
                raise forms.ValidationError('You must be a student to sign up as a student')
        if email and teacher:
            if 'student' in email:
                raise forms.ValidationError('You must be a teacher to sign up as a teacher')



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
