from django.urls import include,path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'student',views.StudentViewSet)
router.register(r'card',views.CardViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
