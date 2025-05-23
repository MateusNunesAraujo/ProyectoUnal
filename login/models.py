from django.contrib.auth.models import User,AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('Empresario', 'Empresario'),
        ('tourist', 'Turista'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tourist')

    # Configurar related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Cambia el nombre relacionado
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Cambia el nombre relacionado
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )