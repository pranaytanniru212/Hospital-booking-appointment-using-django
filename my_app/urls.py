from django.urls import path,include
from django.contrib import admin
from . import views
from .views import AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView
from rest_framework.routers import DefaultRouter

from .views import AppointmentViewSet
router = DefaultRouter()
router.register("appointments", AppointmentViewSet)

urlpatterns = [
    path('', views.home, name='home'),

    path('appointments/', views.appointment_list, name='appointment_list'),

    path('appointment/detail/<int:pk>/',views.appointment_detail,name='appointment_detail'),

    path('appointment/create/',AppointmentCreateView.as_view(),name='appointment_create'),

    path('appointment/update/<int:pk>/',AppointmentUpdateView.as_view(),name='appointment_update'),

    path('appointment/delete/<int:pk>/',AppointmentDeleteView.as_view(),name='appointment_delete'),

    path("api/", include(router.urls)),
]


