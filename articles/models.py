from django.db import models

# Create your models here.
class Article(models.Model):
    # 标题
    headline = models.CharField(max_length = 200)
    # 内容
    content = models.TextField()
    # 发表日志
    update_date = models.DateTimeField()
    # 更新日期
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.headline