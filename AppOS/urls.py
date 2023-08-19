from django.urls import path
from AppOS import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_vista, name='Login'),
    path('logout/', LogoutView.as_view(template_name='AppOS/logout.html'), name='Logout'),
]