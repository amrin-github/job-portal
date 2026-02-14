from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.filters import TitleFilter, CompanyFilter, ApplyCompanyFilter
from new_app.forms import LoginRegister, CompanyForm, JobPostingForm
from new_app.models import Company, Job, ApplyJob, Interview, ProfileDetail, JobSeeker


@login_required(login_url='login_view')
def company_base(request):
    return render(request,'company/company_base.html')

# company form
def company_form(request):
    form1 = LoginRegister()
    form2 = CompanyForm()
    if request.method == "POST":
        form3 = LoginRegister(request.POST)
        form4 = CompanyForm(request.POST)
        if form3.is_valid() and form4.is_valid():
            data1 = form3.save(commit = False)
            data1.is_company = True
            data1.save()

            data2 = form4.save(commit=False)
            data2.user = data1
            data2.save()
            return redirect('login_view')
    return render(request,'company/company_form.html',{'form1':form1,'form2':form2})

# profile
@login_required(login_url='login_view')
def company_profile(request):
    user_data = request.user
    company = Company.objects.get(user=user_data)
    return render(request,'company/profile_view.html',{'company':company})

# edit the profile
@login_required(login_url='login_view')
def edit_company_profile(request,id):
    company = Company.objects.get(id=id)
    form = CompanyForm(instance=company)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_profile')
    return render(request,'company/edit_company_profile.html',{'form':form})

# job posting
@login_required(login_url='login_view')
def job_posting(request):
    user_data = request.user
    job = Company.objects.get(user=user_data)
    if request.method == "POST":
        form = JobPostingForm(request.POST)
        if form.is_valid():
            data = form.save(commit = False)
            data.user = job
            data.save()
            return redirect('company_jobs')
    else:
        form = JobPostingForm()
    return render(request,'company/job_posting.html',{'form':form})

# all the jobs from the company
@login_required(login_url='login_view')
def company_jobs(request):
    today = date.today()
    user_data = request.user
    company_user = Company.objects.get(user=user_data)
    jobs = Job.objects.filter(user=company_user,last_date__gte=today)
    titleFilter = TitleFilter(request.GET, queryset=jobs)
    jobs = titleFilter.qs
    context = {
        'job': jobs,
        'titleFilter': titleFilter
    }

    return render(request,'company/company_jobs.html',context)

# edit company jobs
@login_required(login_url='login_view')
def edit_company_jobs(request,id):
    data = Job.objects.get(id=id)
    form = JobPostingForm(instance=data)
    if request.method == "POST":
        form = JobPostingForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('company_jobs')
    return render(request,'company/edit_company_jobs.html',{'form':form})

# delete jobs
@login_required(login_url='login_view')
def delete_company_jobs(request,id):
    data = Job.objects.get(id=id)
    data.delete()
    return redirect('company_jobs')

# applied jobseeker
@login_required(login_url='login_view')
def applied_jobseekers(request):
    today = date.today()
    user_data = request.user
    company = Company.objects.get(user=user_data)
    job = ApplyJob.objects.filter(job__user=company,applied_date__gte=today)
    applycompanyFilter = ApplyCompanyFilter(request.GET, queryset=job)
    job = applycompanyFilter.qs
    context = {
        'job': job,
        'applycompanyFilter': applycompanyFilter
    }
    return render(request,"company/applied_jobseekers.html", context)

# approve jobseeker
@login_required(login_url='login_view')
def approve_application(request,id):
    data = ApplyJob.objects.get(id=id)
    data.status = 'Approved'
    data.save()
    return redirect('applied_jobseekers')

# reject jobseeker
@login_required(login_url='login_view')
def reject_application(request,id):
    data = ApplyJob.objects.get(id=id)
    data.status = 'Rejected'
    data.save()
    return redirect('applied_jobseekers')

# interview jobseeker
@login_required(login_url='login_view')
def interview_application(request,id):
    data = ApplyJob.objects.get(id=id)
    if request.method == "POST":
        date = request.POST.get('date')
        time = request.POST.get('time')
        Interview.objects.create(interview=data,interview_date=date,interview_time=time)
        data.status = 'Interview'
        data.save()
        if data.exists():
            messages.success(request,'Interview Scheduled successfully')
        return redirect('applied_jobseekers')
    return render(request,'company/interview_form.html',{'interview':data})

# view details of jobseeker
@login_required(login_url='login_view')
def view_details(request,id):
    apply = ProfileDetail.objects.get(id=id)
    return render(request,'company/view_details.html',{'profile_details':apply})

