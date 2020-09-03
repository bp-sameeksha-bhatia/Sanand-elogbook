from django.db import models
from django.urls import reverse
from test.models import Form
from accounts.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    form = models.ForeignKey(Form, on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_role': 'ASSOCIATE'},blank=True,null=True)
    sent_by = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('form', args=(self.form.id,))
        return f'<a href="{url}"> {self.form} </a>'

    @property
    def get_form_id(self):
        return self.form.id


