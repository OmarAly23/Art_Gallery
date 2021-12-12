from django import forms
from .models import ROLE_CHOICES


class MyForm(forms.Form):
	name = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={'placeholder': 'Name', 'maxlength': '100'}
		),
	)
	role = forms.CharField(
		required=True,
		widget=forms.Select(choices=ROLE_CHOICES, attrs={'placeholder': 'role'}),
	)
	email = forms.EmailField(
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Email', 'maxlength': '100'}),
	)
