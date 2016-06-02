from django.test import TestCase
from .models import Organization, Validation, Expert, Region
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

