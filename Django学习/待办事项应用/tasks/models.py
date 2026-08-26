from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # default=1 与迁移 0002_task_user 保持一致（该迁移给已有行填充 user=1），
    # 避免 makemigrations --check 报告缺失 0003；新建数据请显式指定 user
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='tasks', verbose_name="所属用户")
    title = models.CharField(max_length=200, verbose_name="标题")
    description = models.TextField(blank=True, null=True, verbose_name="描述")
    completed = models.BooleanField(default=False, verbose_name="是否完成")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "待办事项"
        verbose_name_plural = "待办事项"

    def __str__(self):
        return self.title
