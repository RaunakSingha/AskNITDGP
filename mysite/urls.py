from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/add/', views.PostCreate.as_view(), name='post-add'),

]
