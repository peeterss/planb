from django.urls import path

from . import views

app_name = 'documentations'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:documentation_code>/', views.detail, name='detail'),
]

