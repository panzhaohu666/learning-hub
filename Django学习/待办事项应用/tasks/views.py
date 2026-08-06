from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task


def user_register(request):
    """用户注册"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 注册后自动登录
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})


def user_login(request):
    """用户登录"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, '用户名或密码错误')
    return render(request, 'tasks/login.html')


def user_logout(request):
    """用户登出"""
    logout(request)
    return redirect('login')


@login_required
def task_list(request):
    """首页：只显示当前用户的任务"""
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        'completed_count': tasks.filter(completed=True).count(),
        'total_count': tasks.count(),
    }
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_create(request):
    """创建新任务"""
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                description=request.POST.get('description', '')
            )
    return redirect('task_list')


@login_required
def task_toggle(request, pk):
    """切换任务的完成状态（仅限自己的任务）"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


@login_required
def task_delete(request, pk):
    """删除任务（仅限自己的任务）"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')


@login_required
def task_clear_completed(request):
    Task.objects.filter(user=request.user, completed=True).delete()
    return redirect('task_list')
