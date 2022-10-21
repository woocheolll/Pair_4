from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('create/', views.create,name='create'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),

]
