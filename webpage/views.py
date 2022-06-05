from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def index(request):
    return render(request,'webpage/index.html')

def control(request):
    return render(request, 'webpage/control.html')

def ingreso(request):
    return render(request, 'webpage/ingreso.html')

def retiro(request):
    return render(request,'webpage/retiro.html')