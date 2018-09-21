from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from django.template.loader import get_template, render_to_string

from website.forms import ContactForm


def home(request):
	return render(request, 'index.html', {})


def projects(request):
	return render(request, 'projects.html', {})


def team(request):
	return render(request, 'team.html', {})


def contact(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact_name = form.cleaned_data['firstName'] + ' ' + form.cleaned_data['lastName'] + ' from ' + form.cleaned_data['organization']
			contact_email = 'contact at: '+form.cleaned_data['email']
			form_content = 'They said: '+ form.cleaned_data['comment']

			message = render_to_string('email.txt', {
				'user': contact_name,
				'group': contact_email,
				'domain': form_content,
			})

			email = EmailMessage('Request Project', message, to=['chscodeforchange@gmail.com'])
			email.send()

			return redirect('/')
		else:
			return render(request, 'contact.html', {'form': form})
	else:
		return render(request, 'contact.html', {'form': form})


def map(request):
	return render(request, 'map.html', {})


def activity(request):
	return render(request, 'activity.html', {})


def keepalive(request):
	return redirect('/map')
