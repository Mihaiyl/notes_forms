"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from notes import views
from django.contrib import admin

urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path('new/', views.NoteCreate.as_view(), name='note_create'),
    path('<int:pk>/edit/', views.NoteEdit.as_view(), name='note_edit'),
    path('<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
]
