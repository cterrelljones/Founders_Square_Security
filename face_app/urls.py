from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('thank_you', views.thank_you),
    path('user_process', views.user_process),
    path('logout_process', views.logout_process),
    path('logout_errors', views.logout_errors),
    path('logout', views.logout),
    path('see_security', views.see_security),
    path('nice_day', views.nice_day),
    path('take_picture', views.take_picture),
    path('sign_in/<int:pic_id>', views.sign_in),
    path('admin_login', views.admin_login),
    path('login_errors', views.login_errors),
]
