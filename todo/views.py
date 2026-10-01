from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import RegisterForm, TaskForm
from .models import Task


# ==========================
# Dashboard
# ==========================

@login_required
def home(request):

    tasks = Task.objects.filter(
        user=request.user
    ).order_by("-created_at")

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(
        status="Completed"
    ).count()

    pending_tasks = tasks.filter(
        status="Pending"
    ).count()

    due_today = tasks.filter(
        due_date=timezone.now().date()
    ).count()

    context = {
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "due_today": due_today,
    }

    return render(
        request,
        "todo/dashboard.html",
        context,
    )
# ==========================
# Register
# ==========================

def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Registration successful!"
            )

            return redirect("home")

    else:

        form = RegisterForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form
        }
    )


# ==========================
# Login
# ==========================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f"Welcome, {user.username}!"
            )

            return redirect("home")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(
        request,
        "registration/login.html"
    )


# ==========================
# Logout
# ==========================

@login_required
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect("login")


# ==========================
# Add Task
# ==========================

@login_required
def add_task(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.user = request.user

            task.save()

            messages.success(
                request,
                "Task added successfully!"
            )

            return redirect("home")

    else:

        form = TaskForm()

    return render(
        request,
        "todo/add_task.html",
        {
            "form": form
        }
    )

@login_required
def edit_task(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Task updated successfully!"
            )

            return redirect("home")

    else:

        form = TaskForm(instance=task)

    return render(
        request,
        "todo/edit_task.html",
        {
            "form": form,
            "task": task
        }
    )

@login_required
def delete_task(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        task.delete()

        messages.success(
            request,
            "Task deleted successfully!"
        )

        return redirect("home")

    return render(
        request,
        "todo/delete_task.html",
        {
            "task": task
        }
    )