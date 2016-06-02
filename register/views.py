from django.shortcuts import get_object_or_404, render, redirect

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import Expert, Validation
import pdfkit

def main(request):
	expert_lst = Expert.objects.all()

	context = {'experts' : expert_lst}

	return render(request, 'register/main_page.html', context)

def validation(request, expert_id):
	expert = Expert.objects.get(id=expert_id)
	validations = Validation.objects.filter(expert=expert)

	if 'to_pdf_btn' in request.GET:
		context = {'validations' : validations, 'organization' : expert.organization, 'export_mode' : True}
		return render_to_pdf('register/validation_page.html', context)
	
	context = {'validations' : validations, 'organization' : expert.organization}
	return render(request, 'register/validation_page.html', context)

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    
    options = {
		'page-size': 'Letter',
		'margin-top': '0.75in',
		'margin-right': '0.75in',
		'margin-bottom': '0.75in',
		'margin-left': '0.75in',
		'encoding': "UTF-8"
	}

    pdf = pdfkit.from_string(html, False, options=options)
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    
    return response