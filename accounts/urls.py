from django.urls import path,include
from  .import views
from django.contrib.auth import views as view


urlpatterns = [
    # path('register/', views.register, name='register'),
    # path('login/', views.login_user, name='login'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),



]