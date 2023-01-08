from rest_framework import serializers
from .models import *

class CheerSerializer(serializers.ModelSerializer): # 임의 설정
    class Meta: # 임의 설정
        model = Cheer # 임의 설정
        fields = ['id', 'charm', 'author', 'content', 'created_at'] # 임의 설정

class CharmSerializer(serializers.ModelSerializer):
    cheer = CheerSerializer(many=True, read_only=True)
    class Meta:
        model = Charm
        fields = ['id', 'title', 'author', 'content', 'total_cheer', 'cur_cheer', 'is_created', 'created_at', 'deleted_at', 'image', 'cheer']