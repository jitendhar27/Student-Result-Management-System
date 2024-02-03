from django.urls import path
from . import views
urlpatterns=[
    path("ttmhome",views.ttmhome,name="ttmhome"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
]