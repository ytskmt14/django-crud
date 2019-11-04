from django.db import models

from django.urls import reverse

# Create your models here.
class Task(models.Model):
    class Meta:
      db_table = 'task'

    # statusの選択肢を定義
    OPEN = 'OPEN'
    WORK_IN_PROGRESS = 'WIP'
    PENDING = 'PEND'
    DONE = 'DONE'
    STATUS = [
      (OPEN, '新規'),
      (WORK_IN_PROGRESS, '作業中'),
      (PENDING, '保留'),
      (DONE, '完了'),
    ]
    title = models.CharField(verbose_name='タイトル', max_length=50)
    content = models.TextField(verbose_name='詳細')
    status = models.CharField(verbose_name='ステータス', max_length=4,choices=STATUS,default=OPEN)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
      return reverse('todo:index')
