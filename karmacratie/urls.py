from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework import compat
from board import views 

router = routers.DefaultRouter()
router.register(r'ministry', views.MinistryViewSet)
router.register(r'cycle', views.CycleViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
