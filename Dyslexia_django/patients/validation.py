from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )






P_NAMES = ['Mexican', 'Asian', 'American', 'Italian', 'Chinese', 'Thai', 'Pizza', 'Other']

def validate_pname(value):
    cat = value.capitalize()
    if not value in P_NAMES and not cat in P_NAMES:
        raise ValidationError(f"{value} not a valid category")