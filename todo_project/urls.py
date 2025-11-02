# from django.contrib import admin
# from django.urls import path, include
# from todo import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.register_user, name='register_user'),
#     #  path('login/', views.login_user, name='login_user'),
#     # path('logout/', views.logout_user, name='logout_user'),
#     path('todo/', views.home, name='home'),
#     path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
#     path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
# ]

   
# urls.py
from django.urls import path
from todo import views

urlpatterns = [
    path("", views.register_user, name="register_user"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("todo/", views.home, name="home"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]
