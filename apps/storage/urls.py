from django.urls import path

from apps.storage import views

app_name = 'storage'

urlpatterns = [
    path('', views.FileUploadListView.as_view(), name='list'),
    path('upload/', views.FileUploadCreateView.as_view(), name='upload'),
    path('delete/<uuid:pk>/', views.FileUploadDeleteView.as_view(), name='delete'),
]
