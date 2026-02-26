from django.urls import path

from apps.user import views

app_name = 'user'

urlpatterns = [
    path('', views.AccountView.as_view(), name='account'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('password/', views.AccountUpdatePasswordView.as_view(), name='password'),
]
