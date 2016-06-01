from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.encode('utf8')


class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.encode('utf8')


class StageAgency(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.encode('utf8')


class Commission(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.encode('utf8')


class ExpertiseClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.encode('utf8')


class ExpertiseKind(models.Model):
    name = models.CharField(max_length=100)
    expertise_class = models.ForeignKey(ExpertiseClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.encode('utf8')


class ExpertSpeciality(models.Model):
    name = models.CharField(max_length=100)
    expertise_kind = models.ForeignKey(ExpertiseKind, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.encode('utf8')


class Expert(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	patronymic = models.CharField(max_length=100)
	expert_type = models.BooleanField()
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

	def __str__(self):
		return (self.name + " " + self.surname).encode('utf8')


class Validation(models.Model):
    name = models.CharField(max_length=100)
    date_begin = models.DateField('Date begin')
    date_end = models.DateField('Date end')
    is_actually = models.BooleanField()
    expert_speciality = models.ManyToManyField(ExpertSpeciality)
    stage_agency = models.ForeignKey(StageAgency, on_delete=models.CASCADE)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.encode('utf8')