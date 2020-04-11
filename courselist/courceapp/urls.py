from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import CoursesViewset

router = DefaultRouter()

router.register(r'courses', CoursesViewset, base_name='courses')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
