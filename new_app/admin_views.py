from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.filters import CompanyFilter, JobseekerFilter
from new_app.forms import CompanyForm, JobSeekerForm
from new_app.models import Company, JobSeeker, Job

@login_required(login_url='login_view')
def admin_base(request):
    return render(request,'admin/admin_base.html')

# company management
@login_required(login_url='login_view')
def read_company(request):
    data = Company.objects.all()
    companyFilter = CompanyFilter(request.GET, queryset=data)
    data = companyFilter.qs
    context = {
        'data1':data,
        'companyFilter':companyFilter
    }
    return render(request,"admin/read_company.html",context)

# # edit company
# @login_required(login_url='login_view')
# def edit_company(request,id):
#     data = Company.objects.get(id=id)
#     form = CompanyForm(instance=data)
#
#     if request.method == 'POST':
#         form = CompanyForm(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect('read_company')
#
#     return render(request,'admin/edit_company.html',{'form1':form})

# delete company
@login_required(login_url='login_view')
def delete_company(request,id):
    data = Company.objects.get(id=id)
    data.delete()
    return redirect('read_company')

# read jobseeker
@login_required(login_url='login_view')
def read_jobseeker(request):
    data = JobSeeker.objects.all()
    jobseekerFilter = JobseekerFilter(request.GET, queryset=data)
    data = jobseekerFilter.qs
    context = {
        'data1': data,
        'jobseekerFilter': jobseekerFilter
    }
    return render(request,"admin/read_jobseeker.html",context)

# # edit jobseeker
# @login_required(login_url='login_view')
# def edit_jobseeker(request,id):
#     data = JobSeeker.objects.get(id=id)
#     form = JobSeekerForm(instance=data)
#
#     if request.method == 'POST':
#         form = JobSeekerForm(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect('read_jobseeker')
#
#     return render(request,'admin/edit_jobseeker.html',{'form1':form})

# delete jobseeker
@login_required(login_url='login_view')
def delete_jobseeker(request,id):
    data = JobSeeker.objects.get(id=id)
    data.delete()
    return redirect('read_jobseeker')

# all jobs
@login_required(login_url='login_view')
def all_jobs(request):
    today = date.today()
    data = Job.objects.filter(last_date__gte=today)
    return render(request,"admin/all_jobs.html",{'data1':data})
