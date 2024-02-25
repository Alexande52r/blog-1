from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, names='post_list'),
    path('<int:id>/', views.post_detail, names="post_detail")
]
