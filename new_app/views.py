from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
# main page
def home(request):
    return render(request,"home.html")

# dashboard
def dashboard(request):
    return render(request,'dashboard.html')

# login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        # print(username)
        password = request.POST.get('pass')
        # print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_base')
            if user.is_company:
                return redirect('company_base')
            if user.is_user:
                return redirect('jobseeker_base')

        else:
            print('Invalid username or password')
    return render(request,'login.html')

# logout
def logout_view(request):
    logout(request)
    return redirect('home')