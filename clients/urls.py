from django.urls import path

from . import views

urlpatterns = [    
    path('', views.list, name='list'),
    path('new', views.new, name='new'),
    path('<int:id>', views.single, name='single'),
    path('del/<int:id>', views.delete, name='del'),
]
