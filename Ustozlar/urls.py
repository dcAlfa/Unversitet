from django.contrib import admin
from django.urls import path

from App.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asosiy),
    path('ustozlar/', ustoz, name="ustozlar"),
    path('ustoz/<int:son>/', ochir_ustoz),
    path('ustoz-t/<int:ue>/', ustoz_edit),
    path('yonalish/<int:ysh>/', ochir_yonalish),
    path('fan/<int:fn>/', ochir_fan),
    path('fan-t/<int:ft>/', fan_edit),
    path('fanlar/', fan),
    path('birlashma/', yonalish),
]
