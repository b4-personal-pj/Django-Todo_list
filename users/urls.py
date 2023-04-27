
from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='signup_view'),
    path('<int:user_id>/', views.UserView.as_view(), name='user_view'),
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('logout/', views.LogoutView.as_view(), name='logout_view'),
]
