"""
URL configuration for universidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from appu import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('menu/',views.menu, name='menu'),
    path('showprofesor/',views.profesorShow, name='showprofesor'),
    path('newprofesor/',views.profesorNew, name='newprofesor'),
    path('editprofesor/<int:idprofesor>/',views.profesorEdit, name='editprofesor'),
    path('updateprofesor/<int:idprofesor>/',views.profesorUpdate, name='updateprofesor'),
    path('deleteprofesor/<int:idprofesor>/',views.profesorDestroy, name='deleteprofesor'),
    path('showmateria/',views.materiaShow, name='showmateria'),
    path('newmateria/',views.materiaNew, name='newmateria'),
    path('editmateria/<int:idmateria>/',views.materiaEdit, name='editmateria'),
    path('updatemateria/<int:idmateria>/',views.materiaUpdate, name='updatemateria'),
    path('deletemateria/<int:idmateria>/',views.materiaDestroy, name='deletemateria'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
