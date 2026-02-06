from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import LoginRegister, JobSeekerForm, ProfileDetailsForm
from new_app.models import JobSeeker, ProfileDetail, Job, ApplyJob

@login_required(login_url='login_view')
def jobseeker_base(request):
    return render(request,'jobseeker/jobseeker_base.html')

# jobseeker form
def jobseeker_form(request):
    form1 = LoginRegister()
    form2 = JobSeekerForm()
    if request.method == "POST":
        form3 = LoginRegister(request.POST)
        form4 = JobSeekerForm(request.POST)
        if form3.is_valid() and form4.is_valid():
            data1 = form3.save(commit = False)
            data1.is_user = True
            data1.save()

            data2 = form4.save(commit=False)
            data2.user = data1
            data2.save()
            return redirect('login_view')
    return render(request,'jobseeker/jobseeker_form.html',{'form1':form1,'form2':form2})

# profile details
# @login_required(login_url='login_view')
# def registration(request):
#     user_data =request.user
#     profile = JobSeeker.objects.get(user=user_data)
#     if request.method == "POST":
#         form = ProfileDetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.save(commit = False)
#             data.user = profile
#             data.save()
#             return redirect('jobseeker_base')
#     else:
#         form = ProfileDetailsForm()
#
#     return render(request,'jobseeker/profile_details.html',{'form':form})

# profile
@login_required(login_url='login_view')
def jobseeker_profile(request):
    user_data = request.user
    profile_details = ProfileDetail.objects.get(user__user=user_data)
    return render(request,'jobseeker/show_profile.html',{'profile_details':profile_details})

# edit profile
@login_required(login_url='login_view')
def edit_profile(request):
    data1 = JobSeeker.objects.get(user=request.user)
    if ProfileDetail.objects.filter(user=data1).exists():
        data = ProfileDetail.objects.get(user=data1)
    else:
        data = ProfileDetail(user=data1)
    form1 = JobSeekerForm(instance=data1)
    form = ProfileDetailsForm(instance=data)

    if request.method == "POST":
        form1 = JobSeekerForm(request.POST, instance=data1)
        form = ProfileDetailsForm(request.POST, request.FILES, instance=data)

        if form1.is_valid() and form.is_valid():
            form1.save()
            profile = form.save(commit=False)
            profile.user = data1
            profile.save()
            return redirect('jobseeker_profile')

    return render(request, 'jobseeker/edit_profile.html', {'form1': form1,'form': form})

# view all jobs
@login_required(login_url='login_view')
def jobseeker_jobs(request):
    data = Job.objects.all()
    return render(request,'jobseeker/jobseeker_jobs.html',{'data':data})

# apply jobs
@login_required(login_url='login_view')
def apply_jobs(request,id):
    job = Job.objects.get(id=id)
    jobseeker = JobSeeker.objects.get(user=request.user)
    already_applied = ApplyJob.objects.filter(job=job , jobseeker=jobseeker)
    if already_applied.exists():
        messages.info(request, 'Already applied.')
    else:
        ApplyJob.objects.create(job=job, jobseeker=jobseeker)
        messages.success(request, 'Applied successfully.')
    return redirect('jobseeker_jobs')

