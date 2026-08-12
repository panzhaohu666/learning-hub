# Django 完全指南 — 从入门到项目实战

> 更新时间：2026-08-03  
> 主版本：**Django 6.0.7**（2026-07-07，当前最新稳定版） 
> LTS 版本：**Django 5.2.16**（扩展支持至 2028-04，生产推荐）  
> Python 要求：**3.12 / 3.13 / 3.14**（Django 6.0 已放弃 Python < 3.12） 
> 涵盖：基础入门、进阶实战、REST API、部署上线

---

## 目录

1. [Django 概述](#1-django-概述)
2. [环境搭建与第一个项目](#2-环境搭建与第一个项目)
3. [项目结构与核心概念（MVT）](#3-项目结构与核心概念mvt)
4. [模型层（Models）](#4-模型层models)
5. [视图层（Views）](#5-视图层views)
6. [模板层（Templates）](#6-模板层templates)
7. [URL 路由](#7-url-路由)
8. [表单处理（Forms）](#8-表单处理forms)
9. [Admin 管理后台](#9-admin-管理后台)
10. [用户认证系统](#10-用户认证系统)
11. [静态文件与媒体文件](#11-静态文件与媒体文件)
12. [国际化（i18n）](#12-国际化i18n)
13. [中间件（Middleware）](#13-中间件middleware)
14. [测试](#14-测试)
15. [Django REST Framework](#15-django-rest-framework)
16. [项目部署](#16-项目部署)
17. [最佳实践](#17-最佳实践)
18. [常见错误与学习路线](#18-常见错误与学习路线)

---

## 1. Django 概述

### 1.1 版本选择

| 版本 | 状态 | 最新补丁 | 支持期限 |
|--------|------|---------|---------|
| **Django 6.0** | 当前稳定 | 6.0.7（2026-07-07）| 主流支持至 2026-08，扩展至 2027-04 |
| **Django 5.2 LTS** | 🛡️ 长期支持 | 5.2.16（2026-07-07）| 扩展支持至 **2028-04** |

**建议**：新手学习用 5.2 LTS（社区资料最多、最稳定）；新项目用 6.0（新特性多）。两者 90% 代码相同，迁移容易。
### 1.2 什么是 Django？
Django 是一个高级 Python Web 框架，由经验丰富的开发者构建，遵循 **"快速开发、简洁设计"** 的理念。它内置了大量开箱即用的功能：
- **ORM（对象关系映射）**：用 Python 代码操作数据库，无需手写 SQL
- **Admin 后台**：自动生成数据管理界面
- **模板引擎**：前后端不分离时的渲染方式
- **表单处理**：表单生成、验证、HTML 渲染一体化
- **认证系统**：用户注册、登录、权限管理
- **缓存框架**：多后端缓存支持
- **国际化**：多语言支持

### 1.3 Django 6.0 值得关注的新特性
如果你从 4.x 或 5.x 升级，6.0 带来以下变化：
| 特性 | 说明 |
|------|------|
| **主键默认 BigAutoField** | `DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"`，无需手动配置 |
| **CSP 中间件** | 内置 `ContentSecurityPolicyMiddleware`，防 XSS |
| **Template Partials** | `{% partialdef %}` 和 `{% partial %}` 标签，模板组件化 |
| **内置后台任务框架** | `django.tasks` 模块，简单任务无需引入 Celery |
| **现代 Email API** | 基于 `email.message.EmailMessage` 的新邮件接口 |

### 1.4 MVT 架构

Django 采用 **MVT（Model-View-Template）** 架构，是经典 MVC 的变体：

| MVC | MVT（Django）| 职责 |
|-----|---------------|------|
| Model | Model | 数据结构定义，数据库交互 |
| View | Template | 数据展示（HTML 渲染）|
| Controller | View | 业务逻辑，处理请求与响应 |

---

## 2. 环境搭建与第一个项目
### 2.1 安装 Python

Django 是 Python 框架，首先需要 Python 3.12+（Django 6.0 要求）或 3.10+（Django 5.2 LTS）：

```bash
# 检查 Python 版本
python --version
```

### 2.2 创建虚拟环境

**推荐为每个 Django 项目创建独立虚拟环境**，避免依赖冲突：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 2.3 安装 Django

```bash
pip install django

# 验证安装
python -m django --version
# 输出示例: 6.0.7
```

### 2.4 创建第一个项目
```bash
# 创建项目
django-admin startproject myproject

# 进入项目目录
cd myproject
```

生成的结构：

```text
myproject/
    manage.py          # 项目管理命令行工具（不要修改）
    myproject/
        __init__.py
        settings.py    # 项目配置（数据库、静态文件等）
        urls.py        # URL 路由入口
        asgi.py        # ASGI 异步服务器配置
        wsgi.py        # WSGI 部署配置
```

### 2.5 创建应用（App）
Django 项目由多**应用（App）* 组成，每个 app 负责一个独立功能：

```bash
python manage.py startapp blog
```

App 初始结构：
```text
blog/
    __init__.py
    admin.py        # Admin 后台注册
    apps.py         # App 配置
    migrations/     # 数据库迁移文件
        __init__.py
    models.py       # 数据模型
    tests.py        # 测试
    views.py        # 视图函数
```

### 2.6 必备 .gitignore

项目初始化时创建 `.gitignore`：
```gitignore
# Python
__pycache__/
*.py[cod]
*.so
venv/
env/
.venv/

# Django
*.log
*.pot
*.pyc
db.sqlite3
media/
staticfiles/

# 环境变量
.env

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

### 2.7 启动开发服务器

```bash
python manage.py runserver
```

浏览器访问 **http://127.0.0.1:8000/**，看到火箭页面即成功。
---

## 3. 项目结构与核心概念（MVT）
### 3.1 请求处理流程

```text
浏览器请求 URL
    → urls.py（URL 匹配，找到对应 View）        → views.py（业务逻辑处理）            → models.py（读/写数据库）            → template（渲染 HTML）                → 返回 HTTP 响应
```

### 3.2 注册 App

在 `settings.py` 中注册 app：
```python
# myproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册自定义 app
    'blog',
]
```

### 3.3 完整项目结构示例

```text
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py          # 根 URL 配置
        asgi.py
        wsgi.py
    blog/
        __init__.py
        admin.py
        apps.py
        migrations/
        models.py
        views.py
        urls.py          # App 级 URL 配置
        forms.py         # 表单定义（手动创建）
        templates/
            blog/
                detail.html
                index.html
        static/
            blog/
                style.css
    templates/           # 项目级模板
        base.html
    static/              # 项目级静态文件
    media/               # 用户上传文件
```

---

## 4. 模型层（Models）
### 4.1 定义模型

模型是数据的 **唯一、权威来源**，每个模型对应数据库中的一张表。
```python
# blog/models.py
from django.db import models


class Category(models.Model):
    """文章分类"""
    name = models.CharField(max_length=100, verbose_name='分类名')
    slug = models.SlugField(unique=True, verbose_name='URL 别名')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Post(models.Model):
    """博客文章"""
    STATUS_CHOICES = [
        ('draft', '草稿'),
        ('published', '已发布'),
    ]

    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(unique=True, verbose_name='URL 别名')
    content = models.TextField(verbose_name='内容')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name='状态'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='分类'
    )
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
```

### 4.2 常用字段类型

| 字段 | 说明 | 示例 |
|------|------|------|
| `CharField` | 短文本 | `models.CharField(max_length=100)` |
| `TextField` | 长文本 | `models.TextField()` |
| `IntegerField` | 整数 | `models.IntegerField(default=0)` |
| `BooleanField` | 布尔值 | `models.BooleanField(default=False)` |
| `DateTimeField` | 日期时间 | `auto_now_add=True`（创建时） `auto_now=True`（每次保存） |
| `DateField` | 日期 | `models.DateField()` |
| `EmailField` | 邮箱 | `models.EmailField()` |
| `URLField` | URL | `models.URLField()` |
| `SlugField` | URL 友好字符串 | `models.SlugField(unique=True)` |
| `ForeignKey` | 一对多 | `models.ForeignKey(OtherModel, on_delete=models.CASCADE)` |
| `ManyToManyField` | 多对多 | `models.ManyToManyField(OtherModel)` |
| `OneToOneField` | 一对一 | `models.OneToOneField(User, on_delete=models.CASCADE)` |
| `ImageField` | 图片 | `models.ImageField(upload_to='images/')` |
| `FileField` | 文件 | `models.FileField(upload_to='files/')` |
| `DecimalField` | 小数 | `models.DecimalField(max_digits=10, decimal_places=2)` |

### 4.3 数据库迁移
```bash
# 生成迁移文件（类似 git commit）python manage.py makemigrations

# 应用迁移到数据库（类似 git push）python manage.py migrate

# 查看迁移 SQL（预览）
python manage.py sqlmigrate blog 0001
```

### 4.4 ORM 查询速查

```python
# 导入模型
from blog.models import Post, Category

# --- 创建 ---
post = Post.objects.create(title='Hello', content='World', status='published')

# --- 查询 ---
# 全部
Post.objects.all()

# 过滤
Post.objects.filter(status='published')
Post.objects.filter(title__icontains='django')   # 不区分大小写
Post.objects.filter(created_at__year=2026)

# 单个
Post.objects.get(id=1)              # 不存在会抛 DoesNotExist
Post.objects.get_or_create(title='Hello')  # 返回 (obj, created)

# 排除
Post.objects.exclude(status='draft')

# --- 排序 ---
Post.objects.order_by('-created_at')

# --- 限制 ---
Post.objects.all()[:10]             # 前 10 条
# --- 聚合 ---
from django.db.models import Count, Avg, Sum
Post.objects.aggregate(Count('id'))
Post.objects.values('category').annotate(count=Count('id'))

# --- 关联查询 ---
# 正向：文章 → 分类
post = Post.objects.get(id=1)
post.category.name

# 反向：分类 → 文章（用 related_name）category = Category.objects.get(id=1)
category.posts.all()
category.posts.filter(status='published')

# 跨表过滤
Post.objects.filter(category__name='Python')

# --- 更新 ---
Post.objects.filter(id=1).update(status='published')
# 或
post = Post.objects.get(id=1)
post.status = 'published'
post.save()

# --- 删除 ---
Post.objects.filter(id=1).delete()
```

### 4.6 数据库事务
```python
from django.db import transaction

# 方式一：装饰器（整个函数的数据库操作在一个事务中）
@transaction.atomic
def transfer_money(from_account, to_account, amount):
    from_account.balance -= amount
    from_account.save()
    to_account.balance += amount
    to_account.save()
    # 任何异常都会回滚整个事务


# 方式二：上下文管理器（局部事务）
def create_post_with_tags(data):
    with transaction.atomic():
        post = Post.objects.create(**data['post'])
        post.tags.set(data['tags'])
        # 如果 tags 设置失败，post 也会回滚


# 保存点（嵌套事务）
with transaction.atomic():
    post = Post.objects.create(title='Hello')
    try:
        with transaction.atomic():
            post.tags.set(some_tags)  # 可能失败
    except Exception:
        pass  # tags 失败不影响 post 创建
```

### 4.7 Signals（信号）

信号允许解耦的模块在特定事件发生时得到通知。
```python
# blog/signals.py
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post


@receiver(post_save, sender=Post)
def notify_on_publish(sender, instance, created, **kwargs):
    """文章发布时发送通知"""
    if instance.status == 'published':
        if created:
            print(f'新文章发布： {instance.title}')
        else:
            old_status = kwargs.get('update_fields')
            if old_status is None or 'status' in old_status:
                print(f'文章状态变更： {instance.title} → 已发布')


@receiver(pre_delete, sender=Post)
def cleanup_on_delete(sender, instance, **kwargs):
    """文章删除前的清理工作"""
    print(f'即将删除文章: {instance.title}')
    # 例如：清理关联文件、发送日志等
```

注册信号（在 `apps.py` 中导入）：
```python
# blog/apps.py
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import blog.signals  # 确保信号被注册
```

**常用内置信号：**

| 信号 | 触发时机 |
|------|---------|
| `post_save` | 模型 save() 后|
| `pre_save` | 模型 save() 前 |
| `post_delete` | 模型 delete() 后|
| `pre_delete` | 模型 delete() 前 |
| `m2m_changed` | 多对多关系变更|
| `post_migrate` | 迁移完成后|
| `request_started` | HTTP 请求开始时 |
| `request_finished` | HTTP 请求结束后|

### 4.7.1 后台任务（Django 6.0 内置）
Django 6.0 新增了 `django.tasks` 模块，简单场景可替代 Celery。
```python
# settings.py
DJANGO_TASK_BACKEND = 'django.tasks.backends.immediate.ImmediateBackend'
# 生产环境建议替换为 django-tasks 的数据库后端或 Redis 后端


# 定义任务
from django.tasks import task

@task()
def send_welcome_email(user_id):
    from django.contrib.auth.models import User
    user = User.objects.get(id=user_id)
    # 发送欢迎邮件的逻辑（耗时操作）
    print(f'已发送欢迎邮件给 {user.email}')


# 调用任务（异步投递，立即返回）
def register_view(request):
    user = form.save()
    send_welcome_email.enqueue(user.id)  # 异步发送，不阻塞用户请求
    return redirect('welcome')
```

> Celery 仍适用于复杂的分布式任务队列；简单场景（发邮件、生成缩略图）用 `django.tasks` 更简洁。
### 4.8 查询优化

```python
# select_related: 一对一 / 外键（JOIN 查询，减少 SQL 次数）
Post.objects.select_related('category').all()

# prefetch_related: 多对多 / 反向关联（额外查询 + Python 连接）
Post.objects.prefetch_related('tags').all()
```

### 4.9 数据库索引
在 `Meta.indexes` 中为常用查询字段建立索引，显著提升查询速度。
```python
class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)  # 单字段索引
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            # 单字段索引（效果等同于 db_index=True）            models.Index(fields=['status']),

            # 复合索引：按状态 + 时间排序查询
            models.Index(fields=['status', '-created_at'], name='status_date_idx'),

            # 唯一约束（替代 unique=True）            models.UniqueConstraint(fields=['title'], name='unique_title'),
        ]
```

迁移时会自动生成相应的数据库索引。**常用场景**：搜索结果排序、按状态过滤列表、关联查询的外键列。
---

## 5. 视图层（Views）
### 5.1 函数视图（FBV）
简单直观，适合简单场景：

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def post_list(request):
    """文章列表"""
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, slug):
    """文章详情"""
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/detail.html', {'post': post})
```

### 5.2 类视图（CBV）
复用性更强，Django 提供了大量通用视图。
```python
# blog/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    """文章列表"""
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published')


class PostDetailView(DetailView):
    """文章详情"""
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Post.objects.filter(status='published')


class PostCreateView(CreateView):
    """创建文章"""
    model = Post
    template_name = 'blog/create.html'
    fields = ['title', 'slug', 'content', 'category', 'tags']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    """编辑文章"""
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'content', 'category', 'tags']
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    """删除文章"""
    model = Post
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy('post_list')
```

### 5.3 常用通用视图一览
| 视图类 | 用途 |
|--------|------|
| `TemplateView` | 渲染静态模板 |
| `ListView` | 对象列表 + 分页 |
| `DetailView` | 单个对象详情 |
| `CreateView` | 创建对象 |
| `UpdateView` | 更新对象 |
| `DeleteView` | 删除对象 |
| `FormView` | 处理表单 |
| `RedirectView` | 重定向 |

### 5.4 异步视图（Django 6.0）
Django 6.0 支持 `async def` 视图，适合处理并发 I/O 密集型请求：

```python
import asyncio
from django.http import JsonResponse


async def async_view(request):
    """异步视图——适合同时调用多个外部 API"""
    await asyncio.sleep(0.1)  # 模拟异步 I/O
    return JsonResponse({'message': '异步响应'})


# 异步 CBV
from django.views import View
from django.utils.decorators import classonlymethod
import asyncio


class AsyncView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request):
        data = await self.fetch_remote_data()
        return JsonResponse(data)

    async def fetch_remote_data(self):
        await asyncio.sleep(0.1)
        return {'status': 'ok'}
```

> **注意**：异步 ORM 仍在完善中（仅支持 `aget`、`acreate`、`abulk_create` 等少数操作），简单 CRUD 使用同步视图即可。异步视图主要优势在于同时调用多个外部 API、WebSocket 等场景。
>
> **部署异步视图必须使用 ASGI**：Gunicorn（WSGI）无法执行 `async def` 视图。改用：
> ```bash
> pip install uvicorn
> uvicorn myproject.asgi:application --host 0.0.0.0 --port 8000
> ```
> 或混合模式：`gunicorn myproject.asgi:application -k uvicorn.workers.UvicornWorker --workers 4`
---

## 6. 模板层（Templates）
### 6.1 模板配置

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],          # 项目级模板目录
        'APP_DIRS': True,                           # 自动查找 app/templates/
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 6.2 自定义模板标签与过滤器
**自定义过滤器：**

```python
# blog/templatetags/blog_filters.py
from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_filter(text):
    """将 Markdown 文本转为 HTML"""
    html = markdown.markdown(text, extensions=['fenced_code', 'codehilite'])
    return mark_safe(html)


@register.filter
def truncate_chinese(text, length=100):
    """中文字符串截断（按字符数而非单词数）"""
    if len(text) <= length:
        return text
    return text[:length] + '...'


@register.simple_tag
def current_year():
    """返回当前年份"""
    from datetime import datetime
    return datetime.now().year


@register.inclusion_tag('blog/tags/latest_posts.html')
def show_latest_posts(count=5):
    """返回最新文章列表（渲染子模板）"""
    from blog.models import Post
    posts = Post.objects.filter(status='published')[:count]
    return {'posts': posts}
```

模板中使用：

```html+django
{% load blog_filters %}

{# 使用自定义过滤器 #}
{{ post.content|markdown }}
{{ post.title|truncate_chinese:20 }}

{# 使用 simple_tag #}
<p>&copy; {% current_year %} 我的博客</p>

{# 使用 inclusion_tag（自动渲染子模板）#}
{% show_latest_posts 5 %}
```

**注意**：自定义标签需要放在 `templatetags/` 包中，并且需要重启服务器。
### 6.3 模板继承

**基础模板** `templates/base.html`：
```html+django
{% load static %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}我的博客{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <header>
        <nav>
            <a href="{% url 'post_list' %}">首页</a>
            {% if user.is_authenticated %}
                <a href="{% url 'post_create' %}">写文章</a>
                <span>{{ user.username }}</span>
                <form method="post" action="{% url 'logout' %}">
                    {% csrf_token %}
                    <button type="submit">退出</button>
                </form>
            {% else %}
                <a href="{% url 'login' %}">登录</a>
            {% endif %}
        </nav>
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <p>&copy; 2026 我的博客</p>
    </footer>
</body>
</html>
```

**子模板： `blog/templates/blog/index.html`：
```html+django
{% extends 'base.html' %}

{% block title %}文章列表{% endblock %}

{% block content %}
<h1>文章列表</h1>

{% for post in posts %}
    <article>
        <h2><a href="{% url 'post_detail' post.slug %}">{{ post.title }}</a></h2>
        <p class="meta">
            分类: {{ post.category.name }} |
            时间: {{ post.created_at|date:"Y-m-d H:i" }}
        </p>
        <p>{{ post.content|truncatewords:50 }}</p>
    </article>
{% empty %}
    <p>暂无文章。</p>
{% endfor %}

{# 分页 #}
{% if is_paginated %}
<div class="pagination">
    {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">上一页</a>
    {% endif %}

    <span>第 {{ page_obj.number }} / {{ page_obj.paginator.num_pages }} 页</span>

    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">下一页</a>
    {% endif %}
</div>
{% endif %}
{% endblock %}
```

### 6.4 常用模板标签

```html+django
{# 变量输出 #}
{{ variable }}
{{ object.attribute }}

{# 过滤器#}
{{ name|lower }}
{{ content|truncatewords:30 }}
{{ date|date:"Y-m-d" }}
{{ text|linebreaks }}
{{ value|default:"暂无" }}

{# 条件判断 #}
{% if user.is_authenticated %}
    已登录
{% elif user.is_staff %}
    管理员
{% else %}
    未登录
{% endif %}

{# 循环 #}
{% for item in items %}
    {{ forloop.counter }}. {{ item.name }}
{% empty %}
    无数据
{% endfor %}

{# URL 反向解析 #}
{% url 'post_detail' slug=post.slug %}

{# 静态文件#}
{% load static %}
<img src="{% static 'images/logo.png' %}">

{# CSRF 令牌（POST 表单必须）#}
{% csrf_token %}

{# 包含子模板#}
{% include 'partials/header.html' %}

{# 注释 #}
{# 这是注释，不会出现在 HTML 中#}
```

### 6.5 常用过滤器
| 过滤器 | 作用 | 示例 |
|--------|------|------|
| `date:"Y-m-d"` | 日期格式化 | `{{ post.created_at\|date:"Y-m-d" }}` |
| `truncatewords:30` | 截断字数 | `{{ content\|truncatewords:30 }}` |
| `truncatechars:100` | 截断字符 | `{{ text\|truncatechars:100 }}` |
| `linebreaks` | 换行为 `<p>` | `{{ content\|linebreaks }}` |
| `lower` / `upper` | 大小写 | `{{ name\|lower }}` |
| `default:"默认"` | 默认值 | `{{ value\|default:"暂无" }}` |
| `length` | 长度 | `{{ list\|length }}` |
| `pluralize` | 复数 | `{{ count }} item{{ count\|pluralize }}` |

### 6.6 Template Partials（Django 6.0 组件化模板）

Django 6.0 新增了 `{% partialdef %}` 和 `{% partial %}` 标签，让模板组件化更简单：

```html+django
{# components/post_card.html — 定义可复用的文章卡片组件 #}
{% partialdef post_card %}
<article class="card">
    <h3>{{ post.title }}</h3>
    <p>{{ post.content|truncatechars:100 }}</p>
    <span>{{ post.created_at|date:"Y-m-d" }}</span>
</article>
{% endpartialdef %}
```

```html+django
{# blog/index.html — 在页面中使用组件 #}
{% extends 'base.html' %}
{% load partials %}

{% block content %}
<h1>文章列表</h1>

{% for post in posts %}
    {# 传统方式：需要遍历中完整 HTML #}
    {% partial post_card %}  {# 一行搞定，自动使用当前作用域的 post 变量 #}
{% endfor %}

{# 也可显式传参：{% partial post_card with post=item %} #}
{% endblock %}
```
**优势**：与 `{% include %}` 不同，partial 共享父模板的作用域，无需手动传参；适合列表项、卡片等高频复用的 UI 片段。

**跨模板复用**：在 `base.html` 中定义全局 partial，所有页面共享：

```html+django
{# base.html — 定义全局组件 #}
{% partialdef header %}
<header>
    <h1>{{ site_title }}</h1>
    <nav>{% partialdef nav %}{% endpartialdef %}</nav>
</header>
{% endpartialdef %}
```

```html+django
{# 任意子模板中使用 #}
{% extends 'base.html' %}
{% partial header %}  {# 自动继承 base.html 中定义的 partial #}

{% block content %}...{% endblock %}
```

---

## 7. URL 路由

### 7.1 基本配置

```python
# myproject/urls.py — 项目根路由from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),           # 包含 app 路由
    path('accounts/', include('django.contrib.auth.urls')),  # 内置认证路由
]
```

### 7.2 App 级路由
```python
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'  # 命名空间（重要！）
urlpatterns = [
    # 函数视图
    path('', views.post_list, name='post_list'),

    # 类视图
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
```

### 7.3 路径转换器
| 转换器 | 匹配 |
|--------|------|
| `str` | 非空字符串（默认值 |
| `int` | 正整数|
| `slug` | 字母数字 + 连字符 + 下划线|
| `uuid` | UUID 格式 |
| `path` | 完整路径（含 `/`）|

```python
path('post/<int:pk>/', views.detail)       # /post/5/
path('post/<slug:slug>/', views.detail)    # /post/hello-world/
path('post/<uuid:id>/', views.detail)      # /post/550e8400-e29b-...
```

### 7.4 反向 URL 解析

```python
# 模板中：
{% url 'blog:post_detail' slug=post.slug %}

# Python 代码中：from django.urls import reverse
url = reverse('blog:post_detail', kwargs={'slug': 'hello-world'})

# 带命名空间 + 绝对 URL
from django.shortcuts import redirect
return redirect('blog:post_list')
```

---

## 8. 表单处理（Forms）
### 8.1 定义表单

```python
# blog/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'category', 'tags', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'slug': forms.TextInput(attrs={'placeholder': '自动生成或手动填写'}),
        }
        labels = {
            'title': '文章标题',
            'content': '文章内容',
        }
        help_texts = {
            'slug': '用于 URL 的英文标识，如 hello-django',
        }

    # 自定义验证
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('标题至少 5 个字符')
        return title
```

### 8.2 视图中处理表单
```python
# blog/views.py
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # 保存多对多关系
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()

    return render(request, 'blog/create.html', {'form': form})
```

### 8.3 模板渲染表单

```html+django
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}

    {# 方式一：自动渲染#}
    {{ form.as_p }}

    {# 方式二：手动渲染（推荐，更灵活） #}
    {% for field in form %}
        <div class="form-group">
            {{ field.label_tag }}
            {{ field }}
            {% if field.help_text %}
                <small>{{ field.help_text }}</small>
            {% endif %}
            {% for error in field.errors %}
                <p class="error">{{ error }}</p>
            {% endfor %}
        </div>
    {% endfor %}

    <button type="submit">提交</button>
</form>
```

---

## 9. Admin 管理后台

### 9.1 创建管理员
```bash
python manage.py createsuperuser
# 按提示输入用户名、邮箱、密码
```

访问 **http://127.0.0.1:8000/admin/**

### 9.2 注册模型

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}  # 自动填充 slug
    search_fields = ['name']


class PostInline(admin.TabularInline):
    """在分类页面内联显示文章""
    model = Post
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 列表页显示
    list_display = ['title', 'category', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']  # 侧边过滤器
    search_fields = ['title', 'content']                  # 搜索框
    prepopulated_fields = {'slug': ('title',)}            # 自动 slug
    date_hierarchy = 'created_at'                         # 日期层级导航

    # 编辑页
    fieldsets = [
        ('基本信息', {'fields': ['title', 'slug', 'content']}),
        ('分类与标签, {'fields': ['category', 'tags']}),
        ('状态, {'fields': ['status']}),
    ]
    filter_horizontal = ['tags']  # 多对多选择器
    # 自定义动作
    actions = ['make_published', 'make_draft']

    @admin.action(description='批量发布')
    def make_published(self, request, queryset):
        queryset.update(status='published')

    @admin.action(description='批量改为草稿')
    def make_draft(self, request, queryset):
        queryset.update(status='draft')
```

### 9.3 Admin 常用选项

| 选项 | 作用 |
|------|------|
| `list_display` | 列表页显示的字段 |
| `list_filter` | 右侧过滤器 |
| `search_fields` | 搜索字段 |
| `ordering` | 默认排序 |
| `date_hierarchy` | 日期层级导航 |
| `prepopulated_fields` | 自动填充字段 |
| `readonly_fields` | 只读字段 |
| `fieldsets` | 分组显示字段 |
| `filter_horizontal` | 多对多水平选择器 |
| `raw_id_fields` | 外键搜索输入框 |
| `actions` | 批量操作 |
| `inlines` | 内联关联模型 |

---

## 10. 用户认证系统

### 10.1 内置视图与 URL

Django 内置了完整的认证视图（登录、退出、改密码等），直接包含即可。
```python
# myproject/urls.py
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
```

内置 URL 一览：

| URL | 模板名 | 用途 |
|-----|--------|------|
| `accounts/login/` | `registration/login.html` | 登录 |
| `accounts/logout/` | `registration/logged_out.html` | 退出 |
| `accounts/password_change/` | `registration/password_change_form.html` | 修改密码 |
| `accounts/password_change/done/` | `registration/password_change_done.html` | 修改完成 |
| `accounts/password_reset/` | `registration/password_reset_form.html` | 密码重置 |
| `accounts/password_reset/done/` | `registration/password_reset_done.html` | 重置邮件已发布|
| `accounts/reset/<uidb64>/<token>/` | `registration/password_reset_confirm.html` | 重置确认 |
| `accounts/reset/done/` | `registration/password_reset_complete.html` | 重置完成 |

### 10.2 自定义登录视图
```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('blog:post_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'欢迎回来, {user.username}!')
            return redirect(request.GET.get('next', 'blog:post_list'))
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, '已退出登录')
        return redirect('blog:post_list')
    return render(request, 'accounts/logout_confirm.html')
```

### 10.3 注册视图

```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog:post_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '注册成功!')
            return redirect('blog:post_list')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
```

### 10.4 权限控制

```python
# 视图中使用装饰器
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def my_view(request):
    """只有登录用户能访问""
    pass

# 类视图中使用 Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    # ...
    pass


# 视图中手动检查
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        return redirect('blog:post_list')  # 或返回 403
    # ...
```

### 10.5 模板中检查权限
```html+django
{% if user.is_authenticated %}
    <p>当前用户: {{ user.username }}</p>
    {% if user.is_staff %}
        <a href="/admin/">管理后台</a>
    {% endif %}
{% else %}
    <a href="{% url 'login' %}">登录</a>
{% endif %}

{# 检查对象级别权限#}
{% if user == post.author %}
    <a href="{% url 'blog:post_update' post.slug %}">编辑</a>
{% endif %}
```

### 10.6 密码安全策略

生产环境必须配置密码验证器：

```python
# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': ('username', 'email', 'full_name'),
            'max_similarity': 0.7,  # 密码与用户名/邮箱相似度不能超过 70%
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,  # 最短长度（Django 默认 8，生产建议 12）        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # 拒绝常见弱密码（如 password123、qwerty）    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        # 拒绝纯数字密码    },
]
```

登录限流（防暴力破解）：

```bash
pip install django-ratelimit
```

```python
# blog/views.py
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', method='POST')
def login_view(request):
    # 同一 IP 每分钟最多 5 次 POST 登录请求
    ...
```

---

## 11. 静态文件与媒体文件

### 11.1 静态文件配置
```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',    # 项目级静态文件]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # 收集后的目录（生产环境用）
```

**收集静态文件（生产部署前）：*

```bash
python manage.py collectstatic
```

### 11.2 媒体文件（用户上传）

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

```python
# myproject/urls.py（仅开发环境）
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your urls ...
]

# 开发环境提供 media 文件访问
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 12. 国际化（i18n）
Django 内置完整的多语言支持，只需简单配置即可实现中英文切换。
### 配置

```python
# settings.py
LANGUAGE_CODE = 'zh-hans'       # 默认语言：简体中文
TIME_ZONE = 'Asia/Shanghai'     # 时区

USE_I18N = True                 # 启用国际化
USE_L10N = True                 # 启用本地化
USE_TZ = True                   # 使用时区感知的 datetime
```

### 标记翻译字符串
**Python 代码中：**

```python
from django.utils.translation import gettext as _

def my_view(request):
    msg = _('欢迎访问我的博客')  # 标记为可翻译字符串
    messages.success(request, msg)
```

**模板中：**

```html+django
{% load i18n %}

<h1>{% trans "文章列表" %}</h1>

{% blocktranslate %}
    共有 {{ count }} 篇文章
{% endblocktranslate %}
```

### 生成翻译文件

```bash
# 创建 locale 目录
mkdir -p locale

# 扫描代码中的翻译标记，生成 .po 文件
python manage.py makemessages -l zh_Hans

# 编辑 locale/zh_Hans/LC_MESSAGES/django.po，填写翻译
# 编译 .po 为 .mo
python manage.py compilemessages
```

**Django admin 和内置功能自动支持多语言**——只需设置 `LANGUAGE_CODE`，admin 界面就会切换为对应语言。

### 语言切换

```python
# urls.py — 添加内置语言切换视图
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns += [
    path('i18n/setlang/', set_language, name='set_language'),
]
```

```html+django
{# 模板中的语言切换器 #}
{% load i18n %}
{% get_current_language as CURRENT_LANG %}
{% get_available_languages as LANGUAGES %}

<p>当前语言: {{ CURRENT_LANG }}</p>
<form action="{% url 'set_language' %}" method="post">
    {% csrf_token %}
    <select name="language">
        {% for code, name in LANGUAGES %}
        <option value="{{ code }}" {% if code == CURRENT_LANG %}selected{% endif %}>{{ name }}</option>
        {% endfor %}
    </select>
    <button type="submit">切换</button>
</form>
```

---

## 13. 中间件（Middleware）
中间件是请求/响应处理的 **"洋葱模型"**：
```text
Request → M1 → M2 → M3 → View → M3 → M2 → M1 → Response
```

### 13.1 自定义中间件

```python
# blog/middleware.py
import time
import logging

logger = logging.getLogger(__name__)


class RequestTimingMiddleware:
    """记录每个请求的处理时间""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        logger.info(f'{request.method} {request.path} - {duration:.3f}s')
        response['X-Request-Duration'] = str(duration)
        return response
```

### 13.2 注册中间件
```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.middleware.RequestTimingMiddleware',   # 自定义]
```

**注意**：顺序很重要：- `SecurityMiddleware` 应在最前面
- `SessionMiddleware` 和 `AuthenticationMiddleware` 顺序不可颠倒- 自定义中间件通常加在最后
### 13.3 CSP 中间件（Django 6.0 新特性）

防止 XSS 和资源劫持的内置安全中间件：

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csp.ContentSecurityPolicyMiddleware',  # 紧接 SecurityMiddleware
    # ...
]

# CSP 策略配置
CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        # 脚本只允许本站和 CDN
        "script-src": ["'self'", "https://cdn.jsdelivr.net"],
        # 样式允许本站和 Bootstrap CDN
        "style-src": ["'self'", "https://cdn.jsdelivr.net", "'unsafe-inline'"],
        # 图片允许本站和外部图片
        "img-src": ["'self'", "data:", "https://*.example.com"],
        # 字体允许本站
        "font-src": ["'self'"],
        # 禁止 iframe 被嵌入
        "frame-ancestors": ["'none'"],
    },
    # 只报告不拦截（调试阶段，上线后去掉此行即可开启拦截）
    # "REPORT_ONLY": True,
}
```
**安全配置速查**（Django 自带 + 推荐的安保护）：

| 保护机制 | 自动生效 | 说明 |
|---------|---------|------|
| XSS 防护 | ✅ 模板自动转义 | `{{ variable }}` 默认 HTML 转义 |
| SQL 注入防护 | ✅ ORM 参数化查询 | `.filter(name=user_input)` 自动参数化 |
| CSRF 防护 | ✅ CsrfViewMiddleware | POST 表单需要 `{% csrf_token %}` |
| 点击劫持防护 | ✅ XFrameOptionsMiddleware | 默认 `DENY`，禁止被嵌入 iframe |
| SSL/TLS | ⚙️ 需配置 | `SECURE_SSL_REDIRECT=True`、`SECURE_HSTS_SECONDS=31536000` |
| Cookie 安全 | ⚙️ 需配置 | `SESSION_COOKIE_SECURE=True`、`CSRF_COOKIE_SECURE=True` |
| 暴力破解防护 | 📦 django-ratelimit | 限制登录频率（见 §10.6） |
| 软删除 | 📦 django-safedelete | 标记删除而非物理删除，数据可恢复 |
| 日志脱敏 | ⚙️ 需配置 | 避免在日志中记录密码、Token 等敏感字段 |

---

## 14. 测试

### 14.1 运行测试

```bash
# 运行所有测试python manage.py test

# 运行特定 app 的测试python manage.py test blog

# 运行特定测试文件
python manage.py test blog.tests

# 运行特定测试类/方法
python manage.py test blog.tests.PostModelTest
```

### 14.2 模型测试

```python
# blog/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category


class PostModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Python', slug='python')
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Hello World',
            category=self.category,
            status='published'
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_slug_unique(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Post.objects.create(
                title='Another',
                slug='test-post',  # 重复
                content='...',
                category=self.category
            )
```

### 14.3 视图测试

```python
from django.test import TestCase, Client
from django.urls import reverse


class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Python', slug='python')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Hello World',
            category=self.category,
            status='published'
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_post_detail_view(self):
        response = self.client.get(
            reverse('blog:post_detail', kwargs={'slug': 'test-post'})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World')
```

### 14.4 使用 RequestFactory（隔离测试）

```python
from django.test import RequestFactory, TestCase
from .views import post_list


class PostViewUnitTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_post_list_returns_200(self):
        request = self.factory.get('/blog/')
        response = post_list(request)
        self.assertEqual(response.status_code, 200)
```

### 14.5 推荐测试工具

- **pytest-django**：更简洁的断言语法 + 参数化测试 + 插件生态。安装后 `pip install pytest-django`，设置 `DJANGO_SETTINGS_MODULE` 环境变量即可运行 `pytest`。

**pytest 示例：**

```python
# tests.py 或 test_views.py
import pytest
from django.test import Client
from blog.models import Post

@pytest.mark.django_db
def test_post_list(client):
    response = client.get('/blog/')
    assert response.status_code == 200
    assert 'Test Post' in response.content.decode()

# 参数化测试——一条测试函数覆盖多种输入
@pytest.mark.django_db
@pytest.mark.parametrize('slug,expected_code', [
    ('test-post', 200),
    ('non-existent', 404),
])
def test_post_detail(client, slug, expected_code):
    response = client.get(f'/blog/post/{slug}/')
    assert response.status_code == expected_code
```

- **unittest.mock**：模拟外部 API 调用 `from unittest.mock import patch`，避免测试依赖外部服务。
- **coverage**：`pip install coverage && coverage run -m pytest && coverage html` 生成测试覆盖率报告。
### 14.6 性能测试（可选）

使用 Locust 进行压力测试：
```bash
pip install locust
# 编写 locustfile.py 定义用户行为，然后
locust -f locustfile.py --host=http://127.0.0.1:8000
```

---

## 15. Django REST Framework

### 15.1 安装

```bash
pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
]
```

### 15.2 Serializer（序列化器）

```python
# blog/serializers.py
from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'post_count']

    def get_post_count(self, obj):
        return obj.posts.count()


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content',
            'status', 'category', 'category_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
```

### 15.3 ViewSet（视图集）
```python
# blog/api_views.py
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']

    def get_permissions(self):
        """创建/编辑/删除需要登录，查看不需要""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        """根据查询参数过滤"""
        queryset = Post.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @action(detail=False, methods=['get'])
    def published(self, request):
        """自定义action: /api/posts/published/"""
        posts = self.get_queryset().filter(status='published')
        page = self.paginate_queryset(posts)
        if page is not None:
            return self.get_paginated_response(
                self.get_serializer(page, many=True).data
            )
        return Response(self.get_serializer(posts, many=True).data)
```

### 15.4 Router 配置

```python
# blog/api_urls.py
from rest_framework.routers import DefaultRouter
from .api_views import PostViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='api-post')
router.register(r'categories', CategoryViewSet, basename='api-category')

urlpatterns = router.urls
```

```python
# myproject/urls.py
urlpatterns = [
    # ...
    path('api/', include('blog.api_urls')),
    path('api/auth/', include('rest_framework.urls')),  # DRF 内置登录
]
```

### 15.5 DRF API 端点一览
| 方法 | URL | 动作 |
|------|-----|------|
| `GET` | `/api/posts/` | 列表 |
| `POST` | `/api/posts/` | 创建 |
| `GET` | `/api/posts/{id}/` | 详情 |
| `PUT` | `/api/posts/{id}/` | 完整更新 |
| `PATCH` | `/api/posts/{id}/` | 部分更新 |
| `DELETE` | `/api/posts/{id}/` | 删除 |
| `GET` | `/api/posts/published/` | 自定义action |

### 15.6 DRF 全局配置

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    },
}
```

### 15.7 Token 认证实战

**方式一：DRF 内置 Token**

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework.authtoken',  # Token 认证
]
```

```bash
python manage.py migrate
```

生成 Token：

```python
from rest_framework.authtoken.models import Token

token = Token.objects.create(user=user)
print(token.key)  # 例如: 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

客户端请求：

```http
GET /api/posts/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**方式二：JWT（推荐前后端分离项目）**

```bash
pip install djangorestframework-simplejwt
```

```python
# settings.py
from datetime import timedelta

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
}
```

```python
# urls.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

客户端流程：`POST /api/token/` 获取 access+refresh → 请求头 `Authorization: Bearer <access>` → 过期后用 refresh 换新 access。

---

## 16. 项目部署

### 16.1 部署前检查清单
```bash
python manage.py check --deploy
```

### 16.2 生产环境配置

```python
# settings.py（生产环境需要修改的
# 关闭 DEBUG
DEBUG = False

# 设置允许的主机
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# 安全设置
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 数据库（改用 PostgreSQL 或 MySQL）DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# 静态文件STATIC_ROOT = BASE_DIR / 'staticfiles'

# 邮件配置（Django 6.0 新式 API）MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
        'OPTIONS': {
            'host': 'smtp.example.com',
            'port': 587,
            'use_tls': True,
            'username': 'your-email@example.com',
            'password': 'your-password',
        },
    },
}
```

发送邮件示例：

```python
# 使用 Django 6.0 的现代 EmailMessage API
from django.core.mail import EmailMessage

email = EmailMessage(
    subject='欢迎注册我的博客',
    body='感谢注册，请点击以下链接激活账号...',
    from_email='noreply@example.com',
    to=['user@example.com'],
    reply_to=['support@example.com'],
)
email.send()
```

### 16.3 使用环境变量管理敏感信息

推荐使用 `python-decouple` 或 `django-environ`：
**方式 A：python-decouple**（轻量级）
```python
# pip install python-decouple
# settings.py
from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
```

**方式 B：django-environ**（功能更全，支持 URL 解析）
```python
# pip install django-environ
# settings.py
import environ

env = environ.Env()
environ.Env.read_env()  # 读取 .env 文件

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)
DATABASES = {
    'default': env.db(),
}
```

```bash
# .env 文件（不要提交到 Git！）
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgres://user:password@localhost:5432/mydb
```

### 16.4 部署方式

**方式一：Gunicorn + systemd（入门级单机部署，推荐初学者首选）**

无需 Nginx，使用 WhiteNoise 处理静态文件，systemd 守护进程。
```bash
# 安装
pip install gunicorn whitenoise
```

`settings.py` 中加入 WhiteNoise：
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 紧接 SecurityMiddleware 之后
    # ...
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 启用压缩 + 文件名哈希（缓存友好的指纹 URL）
STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
```

systemd 服务文件 `/etc/systemd/system/myproject.service`：
```ini
[Unit]
Description=My Django Project
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/myproject
EnvironmentFile=/path/to/myproject/.env           # 从文件读取环境变量（更安全）
Environment="DJANGO_SETTINGS_MODULE=myproject.settings.production"
ExecStart=/path/to/venv/bin/gunicorn myproject.wsgi:application \
    --bind 0.0.0.0:8000 --workers 4 --timeout 120
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now myproject
```

**方式二：Gunicorn + Nginx（生产级单机，需要 HTTPS/大流量）**

```bash
# 安装
pip install gunicorn

# 运行
gunicorn myproject.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 120
```

Nginx 配置：
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /static/ {
        alias /path/to/staticfiles/;
    }

    location /media/ {
        alias /path/to/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

**方式三：Docker**

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 4
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:16
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword

  nginx:
    image: nginx:alpine
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - static_volume:/staticfiles
    ports:
      - "80:80"
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
```

---

## 17. 最佳实践
### 17.1 项目最佳实践
1. **一个 App 只做一件事**：Blog（博客）、Accounts（账户）、Shop（商城）各司其职
2. **使用自定义User 模型**：项目开始就用 AbstractUser 扩展，后期切换极难3. **settings 分环境*：`settings/base.py`、`dev.py` / `prod.py`
4. **写测试：：至少覆盖核心业务逻辑和 API
5. **使用 django-debug-toolbar**：开发时检查 SQL 查询和性能
6. **Git 忽略敏感文件**：`.env`、`*.pyc`、`media/`、`staticfiles/`

### 17.1.1 Logging 配置

生产环境必备的日志配置：

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/django.log',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
```

使用：
```python
import logging
logger = logging.getLogger(__name__)

def my_view(request):
    logger.info(f'用户 {request.user} 访问了页面')
    try:
        # 业务逻辑
        pass
    except Exception as e:
        logger.error(f'处理请求失败: {e}', exc_info=True)
        raise
```

### 17.1.2 缓存框架

Django 内置强大的缓存系统，支持多种后端。
```python
# settings.py — 开发环境用本地内存缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# 生产环境推荐 Redis（需 pip install django-redis）CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

**三种使用方式：*

```python
# 方式一：页面缓存（URL 级别）from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 缓存 15 分钟
def post_list(request):
    ...


# 方式二：低级缓存 API（任意数据）
from django.core.cache import cache

def get_top_posts():
    cache_key = 'top_posts_10'
    result = cache.get(cache_key)
    if result is None:
        result = Post.objects.filter(status='published').order_by('-views')[:10]
        cache.set(cache_key, result, timeout=300)  # 缓存 5 分钟
    return result


# 方式三：模板片段缓存
```

```html+django
{% load cache %}
{% cache 300 sidebar %}  {# 缓存 300 秒#}
<div class="sidebar">
    {# 耗时的数据库查询或渲染内容#}
    {% show_latest_posts 10 %}
</div>
{% endcache %}
```

> **进阶推荐**：生产环境可使用 `django-cacheops`（自动缓存 ORM 查询，无需手动写缓存代码）或 `django-cachalot`。Redis 集群/哨兵模式配置见 [django-redis 文档](https://github.com/jazzband/django-redis)。

### 17.2 代码格式化
推荐配置，保证团队代码风格统一。
```bash
pip install black isort flake8
```

```ini
# pyproject.toml
[tool.black]
line-length = 100
target-version = ['py312']

[tool.isort]
profile = "black"
line_length = 100

[tool.flake8]
max-line-length = 100
exclude = ["migrations", "venv", ".git", "__pycache__"]
```

```bash
black .          # 自动格式化
isort .           # 自动排序 import
flake8 .          # 检查代码风格问题
```

### 17.3 自定义User 模型

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.username
```

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```

### 17.4 常用第三方库

| 库 | 用途 |
|----|------|
| `djangorestframework` | REST API |
| `django-cors-headers` | 跨域请求 |
| `django-filter` | 高级查询过滤 |
| `django-allauth` | 第三方登录（GitHub/Google 等） |
| `django-debug-toolbar` | 开发调试面板 |
| `django-extensions` | 增强命令（shell_plus 等） |
| `django-storages` | 云存储（S3 等） |
| `celery` | 异步任务 |
| `django-celery-beat` | 定时任务 |
| `pillow` | 图片处理 |
| `django-environ` | 环境变量管理 |
| `whitenoise` | 静态文件服务（简化部署） |
| `sentry-sdk` | 错误监控 |
| `django-prometheus` | 监控指标 |
| `django-htmx` | 轻量级动态前端（无需写 JS） |
| `django-silk` | 请求性能分析 & SQL 耗时追踪 |
| `django-cacheops` | 自动 ORM 查询缓存（Redis 后端） |
| `django-safedelete` | 软删除（标记删除而非物理删除） |
| `djangorestframework-simplejwt` | JWT 认证（前后端分离） |

### 17.5 常用管理命令

```bash
python manage.py startapp app_name          # 创建 app
python manage.py makemigrations             # 生成迁移
python manage.py migrate                    # 应用迁移
python manage.py createsuperuser            # 创建管理员python manage.py collectstatic              # 收集静态文件python manage.py shell                      # Django shell
python manage.py shell_plus                 # 增强 shell（需 django-extensions）python manage.py dbshell                    # 数据库 shell
python manage.py test                       # 运行测试
python manage.py runserver 0.0.0.0:8000     # 启动服务器
python manage.py showmigrations             # 查看迁移状态
python manage.py sqlmigrate app 0001        # 查看迁移 SQL
python manage.py dumpdata app.Model         # 导出数据
python manage.py loaddata file.json         # 导入数据
python manage.py check --deploy             # 部署前检查
```

---

## 18. 常见错误与学习路线
### 18.1 常见错误速查

| 错误 | 原因 | 解决 |
|------|------|------|
| `TemplateDoesNotExist` | 模板路径错误 | 检查 `TEMPLATES['DIRS']` 和 app 目录结构 |
| `OperationalError: no such table` | 未执行迁移 | `python manage.py migrate` |
| `DisallowedHost` | ALLOWED_HOSTS 未配置 | 在 settings.py 中添加域名或 IP |
| `CSRF verification failed` | 表单缺少 csrf_token | 在 POST 表单中添加 `{% csrf_token %}` |
| `AppRegistryNotReady` | apps 未加载完就使用模型 | 检查导入顺序 |
| `ImproperlyConfigured` | 配置缺失 | 确认 INSTALLED_APPS 或 MIDDLEWARE |
| `404 Not Found` | URL 不匹配 | 检查 `urls.py` 配置和命名空间 |
| 静态文件 404（生产） | `STATIC_ROOT` 未收集 | `python manage.py collectstatic`，确认 Web 服务器配置了静态目录 |
| 媒体文件 404（开发） | 未添加 media URL 路由 | 在 `urls.py` 中添加 `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` |
| 跨域 CORS 错误 | 前后端不同域名/端口 | `pip install django-cors-headers`，添加 `'corsheaders'` 到 INSTALLED_APPS 和 MIDDLEWARE |
| 静态文件未更新 | 浏览器缓存 | 使用 `ManifestStaticFilesStorage`（文件名哈希），或按 Ctrl+Shift+R 强制刷新 |

### 18.2 学习路线建议

| 阶段 | 内容 | 预计时间 |
|------|------|----------|
| 第 1 周 | 环境搭建、项目结构、MVT 概念、第一个 Hello World | 2-3 天|
| 第 2 周 | Models、ORM 查询、数据库迁移、Admin 后台 | 3-5 天 |
| 第 3 周 | Views（FBV + CBV）、Templates、URL 路由、表单 | 3-5 天 |
| 第 4 周 | 用户认证、静态文件、中间件、测试 | 3-5 天 |
| 第 5-6 周 | 实战项目：搭建一个完整博客系统 | 1-2 周|
| 第 7-8 周 | Django REST Framework、前后端分离 API | 1-2 周|
| 第 9 周 | 部署（Gunicorn + Nginx + Docker）、性能优化 | 3-5 天|

---

> **推荐资源**
> - **官方文档（简体中文）**：https://docs.djangoproject.com/zh-hans/6.0/ — 官方教程有中文翻译
> - 官方文档（英文）：https://docs.djangoproject.com/en/6.0/
> - Django REST Framework：https://www.django-rest-framework.org/
> - Django Packages：https://djangopackages.org/ （找第三方库）
> - Django 下载页（版本信息）：https://www.djangoproject.com/download/
> - Django News 周刊：https://django-news.com/
> - django-tailwind-cli（免 Node 的 Tailwind）：https://pypi.org/project/django-tailwind-cli/
