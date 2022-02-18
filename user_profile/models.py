from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin, UserManager, Group, Permission
from django.utils.translation import gettext_lazy as _


class ShopUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        blank=True,)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="shop_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="shop_user_set",
        related_query_name="user",
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = (
            ('admin', 'admin'),
            ('staff', 'staff'),
            ('default_user', 'default user')
        )
