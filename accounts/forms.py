from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from . import models



class UserProfileForm(forms.ModelForm):

    # Additional 'confirm e-mail' field against which to 
    # verify first e-mail entry

    confirm_email = forms.EmailField(
        label="Confirm e-mail",
        required=True,
    )

    # Declare 'bio' field in the ModelForm to allow for minimum length
    # validation.

    bio = forms.CharField(widget=forms.Textarea, min_length=10, label="Biography")

    class Meta:
        model = models.UserProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'dob',
            'bio',
            'avatar'
        ]



    def clean(self):
        """Verify that both e-mails received as input
        are the same"""

        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('confirm_email')

        if email != verify:
            raise forms.ValidationError(
                "Please enter the same e-mail in both fields.")
