from django import forms
from nodues import models

class Registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ['username', 'password', 'designation']


class RegProf(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model=models.Prof
        fields = ['department']

class RegHod(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model=models.HeadOfDep
        fields = ['department']

class RegWard(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model=models.Warden
        fields=['hostel']

class RegCare(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model=models.Caretaker
        fields=['hostel']

class RegStud(forms.ModelForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    class Meta:
        model=models.Student
        fields=['first_name','last_name','roll_num','program','department','hostel']


class RegAdmin(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model=models.Administrative
        fields=['department']