from django import forms

class ContactForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=120, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'First Name'}))

    lastName = forms.CharField(label='Last Name', max_length=120, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Last Name'}))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control form',
               'placeholder': 'Email'}))

    organization = forms.CharField(label='Organization Name', max_length=120, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Organization Name'}))
    comment = forms.CharField(label='Comment', widget=forms.Textarea(
        attrs={'type': 'text',
               'class': 'form-control form',
               'rows': 3,
               'placeholder': 'Comment'}))
