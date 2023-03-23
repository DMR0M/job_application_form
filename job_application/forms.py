from django import forms


class ApplicationForm(forms.Form):
	first_name = forms.CharField(max_length=40)
	last_name = forms.CharField(max_length=40)
	email = forms.EmailField(max_length=40)
	date = forms.DateField()
	occupation = forms.CharField(max_length=40)

	def __str__(self):
		return f'{ApplicationForm.__dict__}'
