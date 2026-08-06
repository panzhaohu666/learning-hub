from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # 列表页显示的列
    list_display = ['title', 'completed', 'created_at']
    # 列表页可点击跳转的字段
    list_display_links = ['title']
    # 列表页可编辑的字段（不用点进去就能改）
    list_editable = ['completed']
    # 列表页过滤器
    list_filter = ['completed', 'created_at']
    # 搜索框（按标题搜索）
    search_fields = ['title', 'description']
    # 每页显示数量
    list_per_page = 20
