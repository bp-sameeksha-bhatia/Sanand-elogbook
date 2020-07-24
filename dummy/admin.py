from django.contrib import admin
from .models import Person
import eav

from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin


class PersonAdminForm(BaseDynamicEntityForm):
    model = Person

class PersonAdmin(BaseEntityAdmin):
    form = PersonAdminForm


admin.site.register(Person, PersonAdmin)
