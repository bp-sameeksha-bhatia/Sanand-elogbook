from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AbstractAccessInfoModel(models.Model):
    created = models.DateTimeField(null=True, auto_now_add=True, db_index=True)
    created_by = models.CharField(default='', max_length=255, editable=False)
    modified = models.DateTimeField(null=True, auto_now=True, db_index=True)
    modified_by = models.CharField(default='', max_length=255, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        #update_modified_created_by(self)
        super(AbstractAccessInfoModel, self).save(*args, **kwargs)

class User(AbstractUser, AbstractAccessInfoModel):
    dept = models.TextField(max_length=100)



