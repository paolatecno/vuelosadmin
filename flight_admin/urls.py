"""flight_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
# from django.contrib import admin
from flights.admin import admin_site

from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from flights.models import Vuelo

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VueloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vuelo
		depth = 1
		fields = ('numero', 'fecha', 'hora_salida', 'hora_llegada', 'hora_embarque', 'numero_embarque', 'precio', 'origen', 'destino',)

class VueloViewSet(viewsets.ModelViewSet):
	queryset = Vuelo.objects.all()
	serializer_class = VueloSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vuelos', VueloViewSet)

urlpatterns = [
	# url(r'flights/', include('flights.urls')),
	url(r'^', include(router.urls)),
  url(r'^admin/', admin_site.urls),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
