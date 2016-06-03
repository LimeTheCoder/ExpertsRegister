from django.shortcuts import get_object_or_404, render, redirect

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import Expert, Validation, Region, DergOrgan
import pdfkit
import logging

logger = logging.getLogger(__name__)

def main(request):
	expert_lst = Expert.objects.all()
	msgs = []
	regions = Region.objects.all()
	organs = DergOrgan.objects.all()
	if request.method == 'POST':
		if 'name' in request.POST and request.POST['name'] != "":
			expert_lst = expert_lst.filter(name=request.POST['name'])
			msgs.append('name : ' + request.POST['name'])
		if 'surname' in request.POST and request.POST['surname'] != "":
			expert_lst = expert_lst.filter(surname=request.POST['surname'])
			msgs.append('surname : ' + request.POST['surname'])
		if 'patronymic' in request.POST and request.POST['patronymic'] != "":
			expert_lst = expert_lst.filter(patronymic=request.POST['patronymic'])
			msgs.append('patronymic : ' + request.POST['patronymic'])
		if 'region' in request.POST and request.POST['region'] != 'all':
			reg = Region.objects.get(id=request.POST['region'])
			expert_lst = expert_lst.filter(organization__region=reg)
			msgs.append('region : ' + str(reg))
		if 'organ' in request.POST and request.POST['organ'] != 'all':
			org = DergOrgan.objects.get(id=request.POST['organ'])
			expert_lst = expert_lst.filter(organ=org)
			msgs.append('organ : ' + str(org))
		if 'type' in request.POST and request.POST['type'] != 'all':
			if request.POST['type'] == "True":
				expert_lst = expert_lst.filter(expert_type=True)
			else:
				expert_lst = expert_lst.filter(expert_type=False)
			msgs.append('expert type : ' + request.POST['type'])

	context = {'experts' : expert_lst, 'msgs' : msgs, 'regions' : regions, 'organs' : organs}

	return render(request, 'register/main_page.html', context)

def validation(request, expert_id):
	expert = Expert.objects.get(id=expert_id)
	validations = Validation.objects.filter(expert=expert)
	
	val_params = {}
	for validation in validations:
		specialities = validation.expert_speciality.all()
		uniq_kinds = set([spec.expertise_kind for spec in specialities])
		uniq_classes = set([kind.expertise_class for kind in uniq_kinds])
		val_params['specialities'] = specialities
		val_params['uniq_kinds'] = uniq_kinds
		val_params['uniq_classes'] = uniq_classes

		'''
		val = {}
		
		for exp_class in uniq_classes:
			kinds = set([kind for kind in uniq_kinds if kind.expertise_class == exp_class])
			val[exp_class] = kinds
		val_params.append(val)
		'''

	if 'to_pdf_btn' in request.GET:
		context = {'validations' : validations, 'organization' : expert.organization, 'export_mode' : True, 'params' : val_params}
		return render_to_pdf('register/validation_page.html', context)
	
	context = {'validations' : validations, 'organization' : expert.organization, 'params' : val_params}
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