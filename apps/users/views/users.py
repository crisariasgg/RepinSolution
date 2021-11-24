""" User's Views """

# Django
from django.contrib.auth.views import LoginView
from django.views.generic import View,CreateView,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 
from django.conf import settings
from django.contrib.auth import authenticate,logout,login,get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text


# local Django
from apps.utils.tokens import account_activation_token
from ..forms import SignUpForm
User = get_user_model()


class LoginView(LoginView):
	template_name = 'login.html'

	def post(self, request):
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

			else:
				return HttpResponse("Inactive user.")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)


class IndexView(TemplateView):
	template_name = 'index.html'
	paginate_by = 5
				
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = User.objects.get(pk=self.request.user.pk)
		context.update({
			'user': user,
		})
		return context
	
	def post(self, request):
		pass


class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(settings.LOGIN_URL)


class SignUpView(CreateView):
	form_class = SignUpForm
	template_name = 'signup.html'
	
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False # Deactivate account till it is confirmed
			user.username = user.email # Deactivate account till it is confirmed
			user.save()

			try:
				"""Send account verification link"""
				current_site = get_current_site(request)
				subject = 'Hi {} to LaCarta, please verify your account'.format(user.email)
				from_email = 'LaCarta <noreply@lacarta.com>'
				text_content = 'LaCarta <noreply@lacarta.com>'
				message = render_to_string('account_activation_email.html', {
					'user': user,
					'domain': current_site.domain,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': account_activation_token.make_token(user),
				})
				print('ENTRO ANTES DE enviar correo')
				msg = EmailMessage(subject, message, from_email, [user.email])
				msg.content_subtype = 'html'
				msg.send()
			except Exception as e:
				print('error',e)
			
			
			print('a punto de redireccionar')
			return HttpResponseRedirect(reverse('users:email_confirm'))


		return render(request, self.template_name, {'form': form})


class ActivateAccount(View):
	def get(self, request, uidb64, token, *args, **kwargs):
		try:
			uid = force_text(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=uid)
		except (TypeError, ValueError, OverflowError, User.DoesNotExist):
			user = None

		if user is not None and account_activation_token.check_token(user, token):
			user.is_active = True
			user.email_confirmed = True
			user.save()
			login(request, user)
			messages.success(request, ('Your account have been confirmed.'))
			return HttpResponseRedirect(reverse('users:index'))
		else:
			messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
			return HttpResponseRedirect(reverse('users:login'))


class EmailConfirmView(TemplateView):
	def get(self, request, **kwargs):     
		return render(request, 'email_confirm.html')

	