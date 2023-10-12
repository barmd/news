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