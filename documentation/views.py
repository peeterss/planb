from django.shortcuts import render, get_object_or_404

from .models import Documentation

# Create your views here.

def index(request):
    latest_documentation_list = Documentation.objects.order_by('code')[:10]
    context = { 'latest_documentation_list' : latest_documentation_list }
    return render(request, 'documentations/index.html', context)

def detail(request, documentation_code):
    documentation = get_object_or_404(Documentation, pk=documentation_code)
    return render(request, 'documentations/detail.html', {'documentation': documentation})