from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug_url>/', views.post_detail, name='post_detail'), # first slug is a data type like "int", second is the data value from the previus page
]