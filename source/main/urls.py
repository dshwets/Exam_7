"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, WatchPool, UpdatePool, CreatePool, DeletePoll, CreateChoice,\
    EditChoice,DeleteChoice,CreateAnswer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='main_page'),
    path('poll/watch/<int:pk>/', WatchPool.as_view(), name='watch_poll'),
    path('pool/update/<int:pk>/', UpdatePool.as_view(), name='update_poll'),
    path('poll/create/', CreatePool.as_view(), name='create_poll'),
    path('poll/delete/<int:pk>/', DeletePoll.as_view(), name='delete_poll'),

    path('poll/<int:pk>/addchoie/', CreateChoice.as_view(), name='create_choice'),
    path('choice/edit/<int:pk>/', EditChoice.as_view(), name='edit_choice'),
    path('choice/delete/<int:pk>/', DeleteChoice.as_view(), name='delete_choice'),
    path('pool/<int:pk>/answer/', CreateAnswer.as_view(), name='create_answer')
]
