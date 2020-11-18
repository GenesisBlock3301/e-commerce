from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout as dj_logout
from django.views.generic import View


# def signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         print("Invalid", form)
#         if form.is_valid():
#             form.save(commit=False)
#             username = form.cleaned_data.get('username', '')
#             email = form.cleaned_data.get('email', '')
#             password = form.cleaned_data.get('password2', '')
#             user = User.objects.create_user(username=username, email=email, password=password)
#             user.save()
#             return redirect('/accounts/login/')
#         else:
#             return HttpResponse("Invalid form")
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {'form': form})

class SignupView(View):
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/shop/')

        return render(request, self.template_name, {'form': form})


# def loginView(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user:
#             login(request, user)
#             return redirect('/shop/')
#     return render(request, 'accounts/login.html')

class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        # print("In side Post ",form.is_valid())
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/shop/')
        return render(request, self.template_name, {'form': form})


def Logout(request):
    dj_logout(request)
    return redirect('/shop/')
