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

    path('showestudiante/', views.estudianteShow, name='showestudiante'),
    path('newestudiante/', views.estudianteNew, name='newestudiante'),
    path('editestudiante/<int:idestudiante>/', views.estudianteEdit, name='editestudiante'),
    path('updateestudiante/<int:idestudiante>/', views.estudianteUpdate, name='updateestudiante'),
    path('deleteestudiante/<int:idestudiante>/', views.estudianteDestroy, name='deleteestudiante'),

    path('showcarrera/', views.carreraShow, name='showcarrera'),
    path('newcarrera/', views.carreraNew, name='newcarrera'),
    path('editcarrera/<int:idcarrera>/', views.carreraEdit, name='editcarrera'),
    path('updatecarrera/<int:idcarrera>/', views.carreraUpdate, name='updatecarrera'),
    path('deletecarrera/<int:idcarrera>/', views.carreraDestroy, name='deletecarrera'),

    path('showmateria/',views.materiaShow, name='showmateria'),
    path('newmateria/',views.materiaNew, name='newmateria'),
    path('editmateria/<int:idmateria>/',views.materiaEdit, name='editmateria'),
    path('updatemateria/<int:idmateria>/',views.materiaUpdate, name='updatemateria'),
    path('deletemateria/<int:idmateria>/',views.materiaDestroy, name='deletemateria'),

    path('showaula/', views.aulaShow, name='showaula'),
    path('newaula/', views.aulaNew, name='newaula'),
    path('editaula/<int:idaula>/', views.aulaEdit, name='editaula'),
    path('updateaula/<int:idaula>/', views.aulaUpdate, name='updateaula'),
    path('deleteaula/<int:idaula>/', views.aulaDestroy, name='deleteaula'),

    path('showhorarioestudiante/', views.horarioestudianteShow, name='showhorarioestudiante'),
    path('newhorarioestudiante/', views.horarioestudianteNew, name='newhorarioestudiante'),
    path('edithorarioestudiante/<int:id>/', views.horarioestudianteEdit, name='edithorarioestudiante'),
    path('updatehorarioestudiante/<int:id>/', views.horarioestudianteUpdate, name='updatehorarioestudiante'),
    path('deletehorarioestudiante/<int:id>/', views.horarioestudianteDestroy, name='deletehorarioestudiante'),

    path('showhorarioprofesor/', views.horarioprofesorShow, name='showhorarioprofesor'),
    path('newhorarioprofesor/', views.horarioprofesorNew, name='newhorarioprofesor'),
    path('edithorarioprofesor/<int:id>/', views.horarioprofesorEdit, name='edithorarioprofesor'),
    path('updatehorarioprofesor/<int:id>/', views.horarioprofesorUpdate, name='updatehorarioprofesor'),
    path('deletehorarioprofesor/<int:id>/', views.horarioprofesorDestroy, name='deletehorarioprofesor'),

    path('showcarreraestudiante/', views.carreraestudianteShow, name='showcarreraestudiante'),
    path('newcarreraestudiante/', views.carreraestudianteNew, name='newcarreraestudiante'),
    path('editcarreraestudiante/<int:id>/', views.carreraestudianteEdit, name='editcarreraestudiante'),
    path('updatecarreraestudiante/<int:id>/', views.carreraestudianteUpdate, name='updatecarreraestudiante'),
    path('deletecarreraestudiante/<int:id>/', views.carreraestudianteDestroy, name='deletecarreraestudiante'),

    path('showmateriaprofesor/', views.materiaprofesorShow, name='showmateriaprofesor'),
    path('newmateriaprofesor/', views.materiaprofesorNew, name='newmateriaprofesor'),
    path('editmateriaprofesor/<int:id>/', views.materiaprofesorEdit, name='editmateriaprofesor'),
    path('updatemateriaprofesor/<int:id>/', views.materiaprofesorUpdate, name='updatemateriaprofesor'),
    path('deletemateriaprofesor/<int:id>/', views.materiaprofesorDestroy, name='deletemateriaprofesor'),

    path('shownota/', views.notaShow, name='shownota'),
    path('newnota/', views.notaNew, name='newnota'),
    path('editnota/<int:id>/', views.notaEdit, name='editnota'),
    path('updatenota/<int:id>/', views.notaUpdate, name='updatenota'),
    path('deletenota/<int:id>/', views.notaDestroy, name='deletenota'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
