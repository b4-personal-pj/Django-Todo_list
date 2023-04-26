from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, name=None, gender=None, age=None, introduction=None):
        if not email:
            raise ValueError("회원가입 시 이메일이 필요합니다.")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            age=age,
            introduction=introduction,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    GENDER_CHOICES = [
        ('Male', '남성'),
        ('Female', '여성'),
    ]
    gender = models.CharField(
        max_length=6, 
        choices=GENDER_CHOICES, 
        null=True, 
        blank=True)
    age = models.IntegerField(null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin