
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
]
