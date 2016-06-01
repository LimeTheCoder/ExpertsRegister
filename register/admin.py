from django.contrib import admin
from .models import Region, Organization, Expert, Commission
from .models import Validation, StageAgency, ExpertiseClass
from .models import ExpertiseKind, ExpertSpeciality, DergOrgan

# Register your models here.
admin.site.register(Region)
admin.site.register(Organization)
admin.site.register(Expert)
admin.site.register(Commission)
admin.site.register(Validation)
admin.site.register(StageAgency)
admin.site.register(ExpertiseClass)
admin.site.register(ExpertiseKind)
admin.site.register(ExpertSpeciality)
admin.site.register(DergOrgan)
