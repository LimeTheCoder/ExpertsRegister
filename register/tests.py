from django.test import TestCase
from .models import Organization, Validation, Expert, Region, DergOrgan, ExpertSpeciality, StageAgency
from django.conf import settings
import django.utils
from django.db import IntegrityError
from django.contrib.auth.models import User
# Create your tests here.
class OrganModelTest(TestCase):
	def setUp(self):
		region = Region.objects.create(name='Kyiv')
		Organization.objects.create(name='NDEKTS at the Interior Ministry of Ukraine in Odessa region', address='Kuiv, Polytecnichna st. 56', phoneNumber='070324', region=region)
		Organization.objects.create(name='DNDEKTS MIA of Ukraine', address='Kyiv, Polytecnichna st. 67', phoneNumber='98798332', region=region)

	def test_creation(self):
		organ = Organization.objects.get(name='NDEKTS at the Interior Ministry of Ukraine in Odessa region')
		self.assertIsInstance(organ, Organization)

	def test_string_representation(self):
		organ = Organization.objects.get(name='NDEKTS at the Interior Ministry of Ukraine in Odessa region')
		self.assertEqual(str(organ), organ.name)

	def test_pk(self):
		organ = Organization.objects.get(name='NDEKTS at the Interior Ministry of Ukraine in Odessa region')
		self.assertEqual(organ.pk, 1)

	def test_verbose_name_plural(self):
		self.assertEqual(str(Organization._meta.verbose_name_plural), "organizations")

	def test_obj_cnt(self):
		self.assertEqual(len(Organization.objects.all()), 2)

	def test_copy(self):
		organ = Organization.objects.get(name='NDEKTS at the Interior Ministry of Ukraine in Odessa region')
		organ.pk = None
		organ.save()
		self.assertEqual(len(Organization.objects.filter(name='NDEKTS at the Interior Ministry of Ukraine in Odessa region')), 2)

	def test_delete_method(self):
		organ = Organization.objects.get(name='DNDEKTS MIA of Ukraine')
		organ.delete()
		try:
			obj = Organization.objects.get(name='DNDEKTS MIA of Ukraine')
		except Organization.DoesNotExist:
			obj = None

		self.assertIsNone(obj)

	def test_update_method(self):
		id = 1
		organ = Organization.objects.get(pk=id)
		organ.name='UAS in the Transcarpathian region'
		organ.save()
		updated_org = Organization.objects.get(name='UAS in the Transcarpathian region')
		self.assertEqual(updated_org.id, id)

class ValidationModelTest(TestCase):
	def setUp(self):
		exp_type = True
		region = Region.objects.create(name='Kyiv')
		org = Organization.objects.create(name='NDEKTS at the Interior Ministry of Ukraine in Odessa region', address='Kuiv, Polytecnichna st. 56', phoneNumber='070324', region=region)
		dorg = DergOrgan.objects.create(name='MID')
		exp = Expert.objects.check.create(name='Ivan', surname='Ivanov', patronymic='Ivanovich',expert_type=exp_type,organization=org,organ=dorg)

		actyal = True
		exp_sp=ExpertSpeciality.objects.create(name='Transologichna')
		st_agen=StageAgency.objects.create(name='MVS')

		Validation.objects.create(name='Validation_test', date_begin='2015-12-31', date_end='2016-12-31', is_actually=actyal, expert_speciality=exp_sp, stage_agency=st_agen, expert=exp)
		Validation.objects.create(name='Validation_test_1', date_begin='2015-10-8', date_end='2017-12-31', is_actually=actyal, expert_speciality=exp_sp, stage_agency=st_agen, expert=exp)

	def test_creation(self):
		expert = Validation.objects.get(name='Validation_test')
		self.assertIsInstance(expert, Expert)

	def test_string_representation(self):
		expert = Validation.objects.get(name='Validation_test')
		self.assertEqual(str(expert), expert.name)

	def test_pk(self):
		expert = Validation.objects.get(name='Validation_test')
		self.assertEqual(expert.pk, 1)

	def test_verbose_name_plural(self):
		self.assertEqual(str(Validation._meta.verbose_name_plural), "validation")

	def test_obj_cnt(self):
		self.assertEqual(len(Validation.objects.all()), 2)

	def test_copy(self):
		expert = Validation.objects.get(name='Validation_test')
		expert.pk = None
		expert.save()
		self.assertEqual(len(Validation.objects.filter(name='Validation_test')), 2)

	def test_delete_method(self):
		expert = Validation.objects.get(name='Validation_test_1')
		expert.delete()
		try:
			obj = Validation.objects.get(name='Validation_test_1')
		except Validation.DoesNotExist:
			obj = None

		self.assertIsNone(obj)

	def test_update_method(self):
		id = 1
		expert = Validation.objects.get(pk=id)
		expert.name='Valid_update_test'
		expert.save()
		updated_org = Validation.objects.get(name='Valid_update_test')
		self.assertEqual(updated_org.id, id)

class ExpertModelTest(TestCase):
	def setUp(self):
		exp_type = True
		region = Region.objects.create(name='Kyiv')
		org = Organization.objects.create(name='NDEKTS at the Interior Ministry of Ukraine in Odessa region', address='Kuiv, Polytecnichna st. 56', phoneNumber='070324', region=region)
		dorg = DergOrgan.objects.create(name='MID')
		Expert.objects.check.create(name='Ivan', surname='Ivanov', patronymic='Ivanovich',expert_type=exp_type,organization=org,organ=dorg)
		Expert.objects.check.create(name='Petr', surname='Petrov', patronymic='Petrovich',expert_type=exp_type,organization=org,organ=dorg)

	def test_creation(self):
		expert = Expert.objects.get(name='Ivan')
		self.assertIsInstance(expert, Expert)

	def test_string_representation(self):
		expert = Expert.objects.get(name='Ivan')
		self.assertEqual(str(expert), expert.name)

	def test_pk(self):
		expert = Expert.objects.get(name='Ivan')
		self.assertEqual(expert.pk, 1)

	def test_verbose_name_plural(self):
		self.assertEqual(str(Expert._meta.verbose_name_plural), "expert")

	def test_obj_cnt(self):
		self.assertEqual(len(Expert.objects.all()), 2)

	def test_copy(self):
		expert = Expert.objects.get(name='Ivan')
		expert.pk = None
		expert.save()
		self.assertEqual(len(Expert.objects.filter(name='Ivan')), 2)

	def test_delete_method(self):
		expert = Expert.objects.get(name='Petr')
		expert.delete()
		try:
			obj = Expert.objects.get(name='Petr')
		except Expert.DoesNotExist:
			obj = None

		self.assertIsNone(obj)

	def test_update_method(self):
		id = 1
		expert = Expert.objects.get(pk=id)
		expert.name='Vasya'
		expert.save()
		updated_org = Expert.objects.get(name='Vasya')
		self.assertEqual(updated_org.id, id)