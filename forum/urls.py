
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:comment_id>/', views.comment, name='comment'),
    path('new/', views.new_comment, name='new')
]
