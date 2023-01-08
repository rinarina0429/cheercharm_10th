from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # 임의 설정
    email = models.EmailField(max_length=100, unique=True) # 임의 설정s

class Charm(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 부적 주인
    created_at = models.DateTimeField(auto_now_add=True) # 부적 생성 시기
    deleted_at = models.DateTimeField(null=True, blank=True, default=None) # 부적 삭제 시기
    title = models.CharField(max_length=30) # 부적 제목
    content = models.TextField(max_length=200) # 부적 내용
    total_cheer = models.IntegerField(null=True) # 필요 응원 개수
    cur_cheer = models.PositiveIntegerField(verbose_name='응원수', null=True, blank=True) # 현재 응원 개수 # !!!!!!!!
    is_created = models.BooleanField(default=False) # 완성 여부
    class Image(models.IntegerChoices):
        mouse = 1
        goat = 2
        squirrel = 3
        monkey = 4
        bird = 5
    image = models.IntegerField(choices=Image.choices, blank=True, null=True) # 이미지 선택

class Cheer(models.Model): # 임의 설정
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 임의 설정
    charm = models.ForeignKey(Charm, on_delete=models.CASCADE, related_name='cheer') # 임의 설정
    created_at = models.DateTimeField(auto_now_add=True) # 임의 설정
    content = models.TextField() # 임의 설정