from django.contrib import admin
from django.urls import path, include
from SimpleAPI import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename= 'student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    path('gettoken/', TokenObtainPairView.as_view(), name='obtain_token_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify/', TokenVerifyView.as_view(), name='verify_token'),

]