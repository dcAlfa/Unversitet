from django.contrib import admin
from django.urls import path

from App.views import *


urlpatterns = {
    path('admin/', admin.site.urls),
    path('', asosiy),
    path('ustozlar/', ustoz),
    path('ustoz/<int:son>/', ochir_ustoz),
    path('fanlar/', fan),
}
