from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("sign_up", views.regist, name="regist"),
    path("sign_in", views.vhod, name="vhod"),
    path("sign_out", views.vihod, name="vihod"),
    path("test", views.test, name="test"),
    path("create", views.create, name="create"),
    path("jobs", views.jobs, name="jobs"),
]