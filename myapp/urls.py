from django.contrib import admin
from django.urls import path
from myapp.views import (
    signup, loginpage, home, logoutpage,
    addemployee, viewemployee
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signup, name='signup'),
    path('login/', loginpage, name='login'),
    path('home/', home, name='home'),
    path('logout/', logoutpage, name='logout'),
    path('addemployee/', addemployee, name='addemployee'),
    path('viewemployee/', viewemployee, name='viewemployee'),
]


