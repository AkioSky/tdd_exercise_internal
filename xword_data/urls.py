from django.urls import path
from . import views

app_name = 'xword'

urlpatterns = [
    path('', views.drill, name='drill'),
    path('answer/<pk>/', views.answer, name='answer')
]