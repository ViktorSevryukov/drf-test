from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'auth_core'

urlpatterns = [
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='auth_core/login.html'),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(template_name='auth_core/logout.html'),
        name='logout')
]
