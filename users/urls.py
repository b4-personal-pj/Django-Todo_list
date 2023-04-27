
from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='signup'),
    path('user/', views.UserView.as_view(), name='user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
