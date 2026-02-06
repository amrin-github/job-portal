from django.urls import path

from new_app import views, admin_views, jobseeker_views, company_views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login_view", views.login_view, name="login_view"),
    path("logout_view", views.logout_view, name="logout_view"),

    path("admin_base", admin_views.admin_base, name="admin_base"),
    path("read_company", admin_views.read_company, name="read_company"),
    path("edit_company/<int:id>", admin_views.edit_company, name="edit_company"),
    path("delete_company/<int:id>", admin_views.delete_company, name="delete_company"),
    path("read_jobseeker", admin_views.read_jobseeker, name="read_jobseeker"),
    path("edit_jobseeker/<int:id>", admin_views.edit_jobseeker, name="edit_jobseeker"),
    path("delete_jobseeker/<int:id>", admin_views.delete_jobseeker, name="delete_jobseeker"),
    path("all_jobs", admin_views.all_jobs, name="all_jobs"),

    path("jobseeker_base", jobseeker_views.jobseeker_base, name="jobseeker_base"),
    path("jobseeker_form", jobseeker_views.jobseeker_form, name="jobseeker_form"),
    path("jobseeker_profile", jobseeker_views.jobseeker_profile, name="jobseeker_profile"),
    path("edit_profile", jobseeker_views.edit_profile, name="edit_profile"),
    # path("registration", jobseeker_views.registration, name="registration"),
    path("jobseeker_jobs", jobseeker_views.jobseeker_jobs, name="jobseeker_jobs"),
    path("apply_jobs/<int:id>", jobseeker_views.apply_jobs, name="apply_jobs"),

    path("company_base", company_views.company_base ,name="company_base"),
    path("company_form", company_views.company_form ,name="company_form"),
    path("company_profile", company_views.company_profile ,name="company_profile"),
    path("edit_company_profile/<int:id>", company_views.edit_company_profile ,name="edit_company_profile"),
    path("job_posting", company_views.job_posting ,name="job_posting"),
    path("company_jobs", company_views.company_jobs ,name="company_jobs"),
    path("edit_company_jobs/<int:id>", company_views.edit_company_jobs ,name="edit_company_jobs"),
    path("delete_company_jobs/<int:id>", company_views.delete_company_jobs ,name="delete_company_jobs"),
    path("applied_jobseekers", company_views.applied_jobseekers ,name="applied_jobseekers"),
    path("approve_application/<int:id>", company_views.approve_application ,name="approve_application"),
    path("reject_application/<int:id>", company_views.reject_application ,name="reject_application"),
]