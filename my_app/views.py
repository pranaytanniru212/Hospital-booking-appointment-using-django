from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from .forms import AppointmentForm
from .models import Appointment
from .serializers import AppointmentSerializers
from rest_framework.decorators import api_view
from django.views.generic import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets

# Create your views here.


def home(request):
    appointments = Appointment.objects.all()
    return render(request, "home.html", {'appointments': appointments})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment_detail.html', {'appointment': appointment})

class AppointmentViewSet(viewsets.ModelViewSet):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'book_appointment.html'
    success_url = reverse_lazy('home')

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'update_appointment.html'
    success_url = reverse_lazy('home')


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = "delete_appointment.html"
    success_url = reverse_lazy("home")





