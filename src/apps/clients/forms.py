from datetime import date

from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _

from apps.clients.models import Client


class ClientCreateForm(forms.ModelForm):
    """
    Form for creating new Client object
    """

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'birth_date', 'photo']

    def clean_birth_date(self):
        """
        Validate date
        """
        birth_date = self.cleaned_data['birth_date']
        if birth_date > date.today():
            raise ValidationError(_('Entered date is more then today'))
        return birth_date


class ClientFilterForm(forms.Form):
    """
    Form with filters for clients
    """
    ORDERING_FIELDS = (
        ('first_name', _('first name')),
        ('last_name', _('last name')),
        ('birth_date', _('birth date'))
    )

    BLANK_CHOICE = (('', '--- Choose field ---'),)

    ordering = forms.ChoiceField(choices=BLANK_CHOICE + ORDERING_FIELDS,
                                 label=_("Ordering"), required=False)
    full_name = forms.CharField(label=_("Name"), required=False,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'type name here'}))
