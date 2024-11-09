from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout as logoutuser
from django.contrib.auth.decorators import login_required
from .models import Post
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.


def home(request):
    all_posts = Post.objects.all().order_by("-id")
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get("p", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"posts": page_obj})


@login_required(login_url="login")
def dashboard(request):
    all_posts = Post.objects.all().order_by("-id")
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get("p", 1)
    page_obj = paginator.get_page(page_number)
    #return render (request, 'dashboard.html',{"posts":page_obj})
    return render(request, "demo_dashboard.html", {"posts": page_obj})


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

    context = {"registerform": form}

    #return render (request, 'register.html', context=context)
    return render(request, "demo_register.html", context=context)


def login(request):
    form = LoginForm

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:    
                auth.login(request, user)
                return redirect("dashboard")

    context = {"loginform": form}
    #return render (request, 'login.html', context=context)
    return render(request, "demo_login.html", context=context)


def logout(request):
    logoutuser(request)
    # return redirect("/")
    return redirect("demo")


def search(request):
    query = request.GET.get("q", "")
    posts = Post.objects.filter(post_title__icontains=query)
    # paginator = Paginator(posts,2)
    # page_number = request.GET.get('p',1)
    # page_obj = paginator.get_page(page_number)
    #return render(request, 'search_results.html', {'posts': posts, 'query': query})
    return render(request, "demo_search.html", {"posts": posts, "query": query})


# @login_required(login_url="login")
def description(request, id):
    all_posts = Post.objects.get(id=id)
    #all_posts = get_object_or_404(Post,id=id)
    return render(request, "description.html", {"posts": all_posts})


def demo(request):   
    all_posts = Post.objects.all().order_by("-id")
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get("p", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "demo.html", {"posts": page_obj})
