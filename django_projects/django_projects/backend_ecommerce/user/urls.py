from django.urls import path
from user import views
urlpatterns = [ path('users/profile/', views.UserAccountView.as_view()) ]
