from myapp import views
from django.contrib import admin 
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
  
from .views import Signup ,Home, Loginview ,Search ,logout_request , image_upload_view

app_name = "myapp"   
  
urlpatterns = [ 
    path('', Signup, name="signup" ),
    path('home/',Home ,name="homepage"),
    path('login/',Loginview) ,
    path('search/',Search),
    path('logout', logout_request, name='logout'),
    path('upload/', views.image_upload_view),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


    
