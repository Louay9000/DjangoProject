import django
from django.contrib import admin
import django.contrib
from django.urls import  include, path

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('user/',include('django.contrib.auth.urls')),
    path('user/', include('user.urls')),
    path('', include('evenements.urls')),
]


#configuring the admin tiltes
admin.site.site_header = 'Evenements Administration'
admin.site.site_title = 'Browser'
admin.site.index_title = 'Welcome to Admin Area'
