from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, SignInForm


def home(request):
    return render(request, "users/home.html")


class SignUpView(View):
    form_class = SignUpForm
    initial = {"key": "value"}
    template_name = "users/sign-up.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")

            return redirect(to="/")

        return render(request, self.template_name, {"form": form})


def SignInView(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")

    else:
        form = SignInForm()

    return render(request, 'users/sign-in.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")
