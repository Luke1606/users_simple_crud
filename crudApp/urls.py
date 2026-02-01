from django.urls import path

from crudApp import views

urlpatterns = [
    path('', views.ShowListView.as_view(), name="show"),
    path('save/<str:pk>/', views.save, name="save"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('result/', views.result, name="result"),
]