from django.urls import path
from . import views
urlpatterns = [
    path('',views.quiz_list,name="quiz_list"),
    path('quiz_detail/<int:pk>',views.quiz_detail,name="quiz_detail"),
    path('register/',views.registerUser,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
]
