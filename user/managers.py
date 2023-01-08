from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, MobileNumber, password, **extraargs):
        if not MobileNumber:
            raise ValueError(_("Mobile Number Missing"))
        MobileNumber = MobileNumber
        User = self.model(MobileNumber=MobileNumber, **extraargs)
        User.set_password(password)
        User.save()
        return User

    def create_superuser(self, MobileNumber, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(MobileNumber, password, **extra_fields)