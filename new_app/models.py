from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

# jobseeker
class JobSeeker(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='jobseeker')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()



# company
class Company(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='company')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    location = models.TextField()
    bio = models.TextField()

# company job
class Job(models.Model):
    user = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='details')
    job_title = models.CharField(max_length=20)
    job_description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    job_type = models.CharField(
        max_length=20,
        choices=[('Full Time','Full Time'),('Part Time','Part Time'),('Internship','Internship')]
    )
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    skills = models.CharField(max_length=50)
    experience = models.CharField(max_length=20)
    last_date = models.DateField()

# user profile details
class ProfileDetail(models.Model):
    user = models.ForeignKey(JobSeeker,on_delete=models.CASCADE,related_name='profile_details')
    qualification = models.CharField(max_length=20)
    experience = models.CharField(max_length=20)
    skills = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resume/')
    profile_image = models.ImageField(upload_to='profiles/')

# job application
class ApplyJob(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='apply_job')
    jobseeker = models.ForeignKey(ProfileDetail,on_delete=models.CASCADE,related_name='apply_jobseeker')
    applied_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Applied','Applied'),('Interview','Interview'),('Approved','Approved'),('Rejected','Rejected')],
        default='Applied'
    )

# interview
class Interview(models.Model):
    interview = models.ForeignKey(ApplyJob,on_delete=models.CASCADE,related_name='interview')
    interview_date = models.DateField()
    interview_time = models.TimeField()




