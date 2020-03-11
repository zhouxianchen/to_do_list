from django.urls import path
from . import  views


app_name = 'my_app'
urlpatterns = [
    path('home/',  views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('edit/<plan_id>', views.edit, name='编辑'),
path('delete/<plan_id>/', views.delete, name='删除'),
]
