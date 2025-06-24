from django.shortcuts import render

def toppage_view(request):
  return render(request, 'toppage.html')

def dashboard_view(request):
  return render(request, 'dashboard.html')

def input_view(request):
  return render(request, 'input.html')

def graph_view(request):
  return render(request, 'graph.html')

def settings_view(request):
  return render(request, 'settings.html')

# Create your views here.
