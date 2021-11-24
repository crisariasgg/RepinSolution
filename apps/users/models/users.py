"""Users models."""


# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin


# Third party
from simple_history import register



class User(AbstractUser):
	"""User model.
	Extend from Django's Abstract User, change the username field
	to email and add some extra fields.
	"""
	customer_id = models.CharField(max_length=100, blank=True,null=True)
	email = models.EmailField(
		'email address',
		unique=True,
		error_messages={
			'unique': 'A user with that email already exists.'
		}
	)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name']
	email_confirmed = models.BooleanField(
		'verified',
		default=False,
		help_text='Set to true when the user have verified its email address.'
	)

	def __str__(self):
		"""Return username."""
		return self.email

	def get_short_name(self):
		"""Return username."""
		return self.email

	@property
	def description(self):
		"""Return username."""
		return f"Descripcion para el usuario {self.email}"


admin.site.register(User)
register(User)