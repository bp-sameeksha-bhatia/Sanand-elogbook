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

    USER_ROLES = (
        ("ASSOCIATE", "Associate"),
        ("SUPERVISOR", "Supervisor"),
        ("ADMIN", "Admin"),
    )

    sap_id = models.CharField(max_length=512, blank=True)
    manager_email = models.CharField(max_length=512, blank=True)
    full_name = models.CharField(max_length=512, blank=True)
    user_role = models.CharField(max_length=15, blank=True, choices=USER_ROLES)
    street_address = models.CharField(max_length=512, blank=True)
    locality = models.CharField(max_length=512, blank=True)
    region = models.CharField(max_length=512, blank=True)
    postal_code = models.CharField(max_length=512, blank=True)
    country_code = models.CharField(max_length=512, blank=True)
    title = models.CharField(max_length=512, blank=True)
    dept = models.CharField(max_length=512)
    is_bp = models.BooleanField(default=False)  # check first 2 chars of employeeNum
    org_unit = models.CharField(max_length=512, blank=True)  # orgUnitPath
    photo_url = models.CharField(max_length=2048, blank=True)
    language = models.CharField(max_length=512, default="EN")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    fcm_id = models.CharField(max_length=1000, blank=True)
    is_locked = models.BooleanField(default=False)
    locked_reason = models.CharField(max_length=512, default="", blank=True)
    who_locked = models.CharField(max_length=256, default="", blank=True)
    utc_offset = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    @property
    def get_users_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def get_user_by_username(username):
        return User.objects.get(username=username)

    @staticmethod
    def get_user_by_sap_id(sap_id):
        return User.objects.filter(sap_id=sap_id).first()

    @staticmethod
    def get_user_by_email(email):
        return User.objects.filter(email=email).first()

    @property
    def is_colgate(self):
        if self.is_bp:
            return False
        else:
            return True



