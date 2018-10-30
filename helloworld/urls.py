# helloworld/urls.py
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^login/$', views.LoginPageView.as_view()),
    url(r'^list/$',views.dogsMantainer,name="index"),
    url(r'^register/$',views.RegisterPageView.as_view()),
    url(r'^register/createUser/$',views.createUser, name="Create User"),
    url(r'^register/createDog/$',views.createDogs, name="Create Dog"),
    url(r'^login/iniciar/$',views.login_iniciar,name="iniciar"),
    url(r'^cerrarsesion$',views.cerrar_session,name="cerrar_session"),
    url(r'^register/dogs/$',views.register_dogs,name="register_dogs"),
    url(r'^delete/dogs/(?P<pk>\d+)/$',views.delete_dogs,name="delete_dogs"),
    url(r'^password/recovery/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset_form.html',
            html_email_template_name='password_reset_email.html',
        ),
        name='password_reset',
    ),
    url(
        r'^password/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url='/login/',
            post_reset_login=True,
            template_name='password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),
    url(
        r'^password/recovery/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html',
        ),
        name='password_reset_done',
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
