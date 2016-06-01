from django.shortcuts import get_object_or_404, render, redirect

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def main(request):
	return render(request, 'register/main_page.html')
