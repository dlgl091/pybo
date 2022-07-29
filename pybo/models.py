import os

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 질문 모델
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # imgfile 값이 null이나 비어도 등록 가능
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User,related_name='voter_question') # voter 추가, 추천기능
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    @property
    def update_counter(self):
        self.hit += 1
        self.save()
        return self.hit


# 답변 모델
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

# 댓글 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
