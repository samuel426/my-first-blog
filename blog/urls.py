from django.conf.urls import url  # url로 수정
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  # 빈 경로를 정규 표현식으로 설정
]

