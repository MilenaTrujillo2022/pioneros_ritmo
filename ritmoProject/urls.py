from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from api import views
from api.views.cursoView import curso_api_view,curso_detail_api_view
from api.views.epsView import eps_api_view,eps_detail_api_view
from api.views.estudianteView import estudiante_api_view,estudiante_detail_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    
    path('curso/', curso_api_view, name = 'curso_api_view'),
    path('curso/<int:pk>', curso_detail_api_view, name = 'curso_detail_api_view'),

    path('eps/', eps_api_view, name = 'eps_api_view'),
    path('eps/<int:pk>', eps_detail_api_view, name = 'eps_detail_api_view'),

    path('estudiante/', estudiante_api_view, name = 'estudiante_api_view'),
    path('estudiante/<int:pk>', estudiante_detail_api_view, name = 'estudiante_detail_api_view'),
]
