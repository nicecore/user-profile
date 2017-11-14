from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class SpecialCharValidator(object):

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d digit.') % {
                                  'min_length': self.min_length})
        if not any(char in special_characters for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d special character.') % {
                                  'min_length': self.min_length})

    def get_help_text(self):
        return "Your password must contain at least one digit."


class AlphaCharValidator(object):

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d uppercase letter.') % {
                'min_length': self.min_length})

    def get_help_text(self):
        return "Your password must contain at least one uppercase character."


class NumericCharValidator(object):

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d digit.') % {
                                  'min_length': self.min_length})

    def get_help_text(self):
        return "Your password must contain at least one digit."
