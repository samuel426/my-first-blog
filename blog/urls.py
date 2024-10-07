from django.conf.urls import url  # url로 변경
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  # 빈 경로
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),  # <int:pk> → 정규 표현식으로 변경
    url(r'^post/new/$', views.post_new, name='post_new'),  # 새 글 작성 경로
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),  # 수정 경로
]

