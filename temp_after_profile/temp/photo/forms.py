

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )

    class ProfileForm(forms.Form):
        College = forms.RegexField(regex=r'^[a-zA-Z0-9_ ]*$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                    label=_("college"), error_messages={
                'invalid': _("Enter your college name")})
        branch = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                   label=_("branch"), error_messages={
                'invalid': _("Enter your branch or field of study.")})
        CGPA = forms.RegexField(regex=r'^\d{1,99}$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                   label=_("cgpa"), error_messages={
                'invalid': _("This percentage must be out of 100 .")})
        Skills= forms.RegexField(regex=r'^[a-zA-Z0-9_ ]*$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("skills"))





