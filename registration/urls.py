from django.conf.urls import url
from . import views

app_name = "registration"

urlpatterns = [
    url(r'^$',views.FormView.as_view(),name="index"),
    url(r'^welcome$',views.welcome,name="welcome"),

    url(r'^stud/$',views.StudForm.as_view(),name="stud"),
    url(r'^stud/welcome$',views.studProf,name="studProf"),

    url(r'^prof/$',views.ProfForm.as_view(),name="prof"),
    url(r'^prof/welcome$',views.ProfWel,name="ProfWel"),

    url(r'^hod/$',views.HodForm.as_view(),name="hod"),
    url(r'^hod/welcome$',views.HodWel,name="HodWel"),

    url(r'^caretaker/$',views.CareForm.as_view(),name="care"),
    url(r'^caretaker/welcome$',views.CareWel,name="CareWel"),

    url(r'^warden/$',views.WardForm.as_view(),name="ward"),
    url(r'^warden/welcome$',views.WardWel,name="WardWel"),

    url(r'^administrative/$',views.AdminForm.as_view(),name="ad"),
    url(r'^administrative/welcome$',views.AdminWel,name="AdminWel"),


]
