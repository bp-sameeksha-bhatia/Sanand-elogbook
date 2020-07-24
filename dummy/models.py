from django.db import models
from django.forms import ModelForm
import eav

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age  = models.IntegerField()

    def __str__(self):
        return self.name

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        template  = 'index.html'
eav.register(Person)


