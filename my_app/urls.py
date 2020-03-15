from django.urls import path
from . import  views


app_name = 'my_app'
urlpatterns = [
    path('home/',  views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('search/', views.search, name='搜索'),
    path('edit/<activity_id>', views.edit, name='编辑'),
    path('delete/<activity_id>/', views.delete, name='删除'),
]
