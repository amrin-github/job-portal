import django_filters
from django import forms
from django_filters import CharFilter

from new_app.models import Company, JobSeeker, Job, ApplyJob


# search company name
class CompanyFilter(django_filters.FilterSet):
    name = CharFilter(label='',lookup_expr='icontains',widget=forms.TextInput
    (attrs={'placeholder':'Search Company','class':'form-control'}))
    class Meta:
        model = Company
        fields = ('name',)

# search jobseeker name
class JobseekerFilter(django_filters.FilterSet):
    name = CharFilter(label='',lookup_expr='icontains',widget=forms.TextInput
    (attrs={'placeholder':'Search Name','class':'form-control'}))
    class Meta:
        model = JobSeeker
        fields = ('name',)

# search company title
class TitleFilter(django_filters.FilterSet):
    job_title = CharFilter(label='',lookup_expr='icontains',widget=forms.TextInput
    (attrs={'placeholder':'Search Title','class':'form-control'}))
    class Meta:
        model = Job
        fields = ('job_title',)

# search company name for applications
class ApplyCompanyFilter(django_filters.FilterSet):
    job__user__name = CharFilter(label='',lookup_expr='icontains',widget=forms.TextInput
    (attrs={'placeholder':'Search Company','class':'form-control'}))
    class Meta:
        model = ApplyJob
        fields = ('job__user__name',)

# search company name for interview
class InterCompanyFilter(django_filters.FilterSet):
    interview__job__user__name = CharFilter(label='',lookup_expr='icontains',widget=forms.TextInput
    (attrs={'placeholder':'Search Company','class':'form-control'}))
    class Meta:
        model = ApplyJob
        fields = ('interview__job__user__name',)