from django.urls import path
from .views import *

app_name = 'cheercharm'

urlpatterns = [
    path('charms/', CharmListView.as_view()),
    path('charms/<int:pk>', CharmDetailView.as_view()),
    path('cheers/', CheerView.as_view()), # 임의 설정
]