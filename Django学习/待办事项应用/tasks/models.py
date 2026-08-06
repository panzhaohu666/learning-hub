from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name="所属用户")
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
