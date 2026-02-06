from django import forms
from django.contrib.auth.forms import UserCreationForm

from new_app.models import JobSeeker, Login, Company, Job, ProfileDetail


# login
class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label= "password",widget=forms.PasswordInput)
    password2 = forms.CharField(label= "confirm password",widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username','password1','password2')

# jobseeker form
class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = '__all__'
        exclude = ('user',)

# jobseeker form
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('user',)

# job form
class JobPostingForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('user',)

# profile details
class ProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = ProfileDetail
        fields = '__all__'
        exclude = ('user',)