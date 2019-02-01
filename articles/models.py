from django.db import models

# Create your models here.
class Article(models.Model):
    # 标题
    headline = models.CharField(max_length = 200)
    # 内容
    content = models.TextField()
    # 发表日志
    pub_date = models.DateTimeField(auto_now_add=True, null = True)
    # 更新日期
    update_date = models.DateTimeField(blank = True, null = True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.headline

    