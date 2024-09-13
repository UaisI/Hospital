from django.urls import path

from .my_views import PatientView
from .views import DoctorView, ServiceView, VisitView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urlpatterns = [
#     path('doctor/', views.DoctorListCreateView.as_view())
# ]

urlpatterns = [
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path('doctor/<int:id>',
         DoctorView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
         })
         ),
    path('doctor/<int:id>/patient/',
         DoctorView.as_view({
             'get': 'list_patient'
         })
         ),
    path(
        'Service/',
        ServiceView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path('service/<int:pk>',
         ServiceView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
         })
         ),
    path(
        'Visit/',
        VisitView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path('Visit/<int:pk>',
         VisitView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
         })
         ),
    path(
        'Patient/',
        PatientView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path('Patient/<int:id>',
         PatientView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
         })
         ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
