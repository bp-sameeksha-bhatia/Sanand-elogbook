from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
import itertools
from .models import User
from django.contrib import messages


class UserAdmin(UserAdmin):
    model = User
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_superuser",
        "is_locked",
        "locked_reason",
        "last_login",
    ]
    list_filter = [
        "is_active",
        "is_staff",
        "is_superuser",
        "is_locked",
        "locked_reason",
        "who_locked",
        "last_login",
    ]
    ordering = [
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "last_login",
    ]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                    "full_name",
                    "street_address",
                    "locality",
                    "region",
                    "postal_code",
                    "title",
                    "dept",
                    "ip_phone",
                    "phone",
                    "is_bp",
                    "org_unit",
                    "photo_url",
                    "language",
                    "decimal_format",
                    "date_format",
                    "thousands_format",
                )
            },
        ),
        ("SAP Info", {"fields": ("manager_email", "sap_id")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    def get_form(self, request, obj=None, **kwargs):
        self.fieldsets = self.get_fieldsets(request, obj)
        return super(UserAdmin, self).get_form(request, obj, **kwargs)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        personal_fields = (
            "first_name",
            "last_name",
            "email",
            "full_name",
            "sap_id",
            "street_address",
            "locality",
            "region",
            "postal_code",
            "title",
            "department",
            "ip_phone",
            "phone",
            "is_bp",
            "org_unit",
            "photo_url",
            "language",
            "decimal_format",
            "date_format",
            "thousands_format",
        )
        if request.user.is_superuser:
            user_fields = ("username", "password")
            perm_fields = (
                "is_active",
                "is_staff",
                "is_superuser",
                "is_locked",
                "groups",
                "user_permissions",
            )
            self.readonly_fields = ("last_login", "date_joined")
        else:
            user_fields = ("username",)
            perm_fields = (
                "is_active",
                "is_staff",
                "is_superuser",
                "is_locked",
                "groups",
            )
            self.readonly_fields = (
                "username",
                "password",
                "is_locked",
                "user_permissions",
                "last_login",
                "date_joined",
                "is_staff",
                "is_superuser",
            )

        return [
            (("Login Credentials"), {"fields": user_fields}),
            (("Personal Info"), {"fields": personal_fields}),
            (("Permissions"), {"fields": perm_fields}),
            (("Important Dates"), {"fields": ("last_login", "date_joined")}),
        ]

    def save_model(self, request, obj, form, change):
        if obj.is_superuser:
            if request.user.is_superuser:
                obj.save()
        else:
            obj.is_staff = True
            obj.save()

    def lock_all_users_admin_lock(self, request, queryset):
        counter = 0
        if request.user.username.lower() in itertools.chain(*MANAGERS):
            users = User.objects.all()
            for user in users:
                counter += 1
                user.lock_user("ADMIN_LOCK", request.user.username)
            self.message_user(
                request,
                f"All users({counter}) locked from system with 'ADMIN_LOCK'",
                messages.SUCCESS,
            )
        else:
            self.message_user(
                request,
                "YOU DO NOT HAVE PERMISSION TO PERFORM THIS ACTION!",
                messages.ERROR,
            )

    lock_all_users_admin_lock.short_description = (
        "Lock all users from system(ADMIN_LOCK)"
    )

    def unlock_all_users_admin_lock(self, request, queryset):
        counter = 0
        if request.user.username.lower() in itertools.chain(*MANAGERS):
            users = User.objects.filter(is_locked=True).filter(
                locked_reason="ADMIN_LOCK"
            )
            for user in users:
                counter += 1
                user.unlock_user()
            self.message_user(
                request,
                f"All users({counter}) unlocked from system with 'ADMIN_LOCK'",
                messages.SUCCESS,
            )
        else:
            self.message_user(
                request,
                "YOU DO NOT HAVE PERMISSION TO PERFORM THIS ACTION!",
                messages.ERROR,
            )

    unlock_all_users_admin_lock.short_description = (
        "Unlock all users from system(ADMIN_LOCK)"
    )

    actions = [lock_all_users_admin_lock, unlock_all_users_admin_lock]

    class UserAd(admin.ModelAdmin):
        pass

    admin.site.register(User,UserAd)
