from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text

    # 演示
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # 用ForeignKey定义了一个关系，告诉Django，每一个Choice对象都关联到一个Question对象
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # [-2147483648,2147483647 ]的取值范围对Django所支持的数据库都是安全的。
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
