from django.shortcuts import get_object_or_404, render, redirect

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import Expert

def main(request):
	expert_lst = Expert.objects.all()

	context = {'experts' : expert_lst}

	return render(request, 'register/main_page.html', context)
