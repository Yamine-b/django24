from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('machines/',views.machine_list_view,name='machines'),
    path('machine/<pk>',views.machine_detail_view,name='machine-detail'),
    path('add-machine',views.machine_add_form,name='add-machine'),
    path('GES/', views.GES, name='GES'),
    path('NAQ/', views.NAQ, name='NAQ'),
    path('ARA/', views.ARA, name='ARA'),
    path('BFC/', views.BFC, name='BFC'),
    path('BRE/', views.BRE, name='BRE'),
    path('CVL/', views.CVL, name='CVL'),
    path('COR/', views.COR, name='COR'),
    path('IDF/', views.IDF, name='IDF'),
    path('OCC/', views.OCC, name='OCC'),
    path('HDF/', views.HDF, name='HDF'),
    path('NOR/', views.NOR, name='NOR'),
    path('PDL/', views.PDL, name='PDL'),
    path('PAC/', views.PAC, name='PAC'),

]