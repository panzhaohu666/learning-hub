from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
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
    """用户登录。

    用 request.POST.get 而不是 request.POST[...]：后者缺字段时抛 KeyError
    直接变 500。next 参数用于登录后跳回原页面，必须校验目标主机，
    否则是开放重定向（攻击者构造 ?next=https://evil.example 把人导出去）。
    """
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        if not username or not password:
            messages.error(request, '用户名和密码不能为空')
            return render(request, 'tasks/login.html', {'next': request.POST.get('next', '')})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}
            ):
                return redirect(next_url)
            return redirect('task_list')
        messages.error(request, '用户名或密码错误')
    return render(request, 'tasks/login.html', {'next': request.GET.get('next', '')})


@require_POST
def user_logout(request):
    """用户登出。

    只接受 POST：GET 能被浏览器预取、图片 src、外链等触发，
    那样用户会在不知情的情况下被登出（会话被销毁）。
    """
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
        title = (request.POST.get('title') or '').strip()
        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                description=(request.POST.get('description') or '').strip()
            )
    return redirect('task_list')


@login_required
@require_POST
def task_toggle(request, pk):
    """切换任务的完成状态（仅限自己的任务）"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


@login_required
@require_POST
def task_delete(request, pk):
    """删除任务（仅限自己的任务）"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')


@login_required
@require_POST
def task_clear_completed(request):
    Task.objects.filter(user=request.user, completed=True).delete()
    return redirect('task_list')
