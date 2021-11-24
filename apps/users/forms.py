# Django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
	class Meta:
		fields = ('email','password1','password2')
		model = get_user_model()
		
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		# self.fields['username'].label = 'Usuario'
		self.fields['email'].label = 'Correo electrónico'
		for fieldname in ['email', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

		