from django.urls import path
from ManyRoles import views
from django.contrib.auth import views as ad


urlpatterns = [
    path('',views.home,name="hme"),
    path('lg/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
    path('lgo/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgt"),
    path('rg/',views.register,name="rgt"),

]