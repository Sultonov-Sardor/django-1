from django.urls import path
from . import views
from django.urls import path, include
from django.contrib import admin

app_name = 'blog'

urlpatterns = [
 # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    views.post_detail,
    name='post_detail'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]

urlpatterns = [
 path('admin/', admin.site.urls),
 path('blog/', include('blog.urls', namespace='blog')),
]