from django.conf.urls import url
from . import views

app_name = 'cms'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'(?P<nombre>.*)/(?P<recurso>.*)$', views.agregar, name="agregar"),
]