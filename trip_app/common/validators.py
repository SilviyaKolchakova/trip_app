from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            # Invalid case
            raise ValidationError('Value must contain only letters')

    # TODO check if driver/vehicle is available in the given period
def get_available_items():
    pass