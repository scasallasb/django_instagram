
#Django
from django.contrib import admin
from django.urls import path


#local views
from instagram import view as local_view
#posts views
from posts import views as posts_views
#user views
from user import views as user_views


#static
from django.conf.urls.static import static

#config settings 

from django.conf import settings
""" importamos vistas"""

urlpatterns = [
    #local views
    path('hola_mundo/', local_view.hello_world, name ='hello_world'),
    path('reto/', local_view.hi),
    path('hi/<str:name>/<int:age>/', local_view.say_hi),
    

   
    #post views
    path('posts/', posts_views.list_post),
    path('posts1/', posts_views.list_post1, name ='feed'),
    

    #user admin 
    path('admin/', admin.site.urls),
    path('users/login', user_views.login_view, name ='login'),
    path('users/logout', user_views.logout_view, name ='logout'),
    path('users/signup/', user_views.signup, name='signup'),

    path ('users/me/profile/',user_views.update_profile, name='update_profile'),

# add url static
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


