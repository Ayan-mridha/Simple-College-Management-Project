from django.contrib import admin
from django.urls import path
from myApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage,name="mainpage"),
    path('studentPage/', studentPage,name="studentPage"),
    path('teacherPage/', teacherPage,name="teacherPage"),
]
