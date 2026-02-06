from django.contrib import admin

from new_app import models

# Register your models here.
admin.site.register(models.JobSeeker)
admin.site.register(models.Company)
admin.site.register(models.Job)
admin.site.register(models.ProfileDetail)
admin.site.register(models.ApplyJob)