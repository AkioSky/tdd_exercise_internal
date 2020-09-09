from django.urls import path
from . import views

app_name = 'xword_data'

urlpatterns = [
    path('', views.drill, name='drill'),
    path('answer/', views.answer, name='answer')
]