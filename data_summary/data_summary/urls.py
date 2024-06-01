from django.contrib import admin
from django.urls import path
from summary.views import summary_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', summary_view, name='summary_view'),
]
