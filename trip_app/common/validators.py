from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha() or ch.isspace():
            # Invalid case
            raise ValidationError('Value must contain only letters')


def validate_min_price_per_km(value):
    if value < 1.00:
        raise ValidationError(
            f'Lowest possible price is BGN 1.00')


def validate_min_distance(value):
    if value < 20:
        raise ValidationError(
            f'The minimum distance is 20 km')

    # TODO check if driver/vehicle is available in the given period
def get_available_items():
    pass