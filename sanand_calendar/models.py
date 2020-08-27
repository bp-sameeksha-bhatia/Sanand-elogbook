from django.db import models
from test.models import Form
from accounts.models import User
# Create your models here.
from  django.utils.timezone import timezone
class Schedule(models.Model):
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'user_role':'ASSOCIATE'})
    sent_by = models.CharField(max_length=300)
    submit_by = models.DateField(null=True,blank=True,default='')

    def __str__(self):
        return f"{self.form.form_name} sent by {self.sent_by} ,submit before: {self.submit_by}"







