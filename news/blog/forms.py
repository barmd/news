from django import forms
from blog.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'email',
            'name',
            'phone',
            'subject',
            'message',
        ]

class PostSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)