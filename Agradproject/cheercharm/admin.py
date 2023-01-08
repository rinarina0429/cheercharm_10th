from django.contrib import admin
from .models import User, Charm, Cheer

# Register your models here.
admin.site.register(User) # 임의 설정
admin.site.register(Charm)
admin.site.register(Cheer) # 임의 설정