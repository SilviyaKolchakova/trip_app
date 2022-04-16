import unittest
from django.core.exceptions import ValidationError

from trip_app.common.validators import validate_only_letters, validate_min_price_per_km, validate_min_distance


class OnlyLettersValidatorTest(unittest.TestCase):

    def test_only_letters_validator_whenOneDigit_shouldRaise(self):
        NON_VALID_ELEMENT = 'Maria4'
        with self.assertRaises(ValidationError) as context:
            validate_only_letters(NON_VALID_ELEMENT)
        self.assertIsNotNone(context.exception)

    def test_only_letters_validator_when_only_letters_should_do_nothing(self):
        VALID_ELEMENT = 'Maria'
        validate_only_letters(VALID_ELEMENT)
        self.assertTrue(True)


class MinPricePerKmValidatorTest(unittest.TestCase):

    def test_min_price_per_km_validator_when_lower_value_should_raise(self):
        with self.assertRaises(ValidationError) as context:
            validate_min_price_per_km(0.6)
        self.assertIsNotNone(context.exception)

    def test_only_letters_validator_when_correct_value_should_do_nothing(self):

        validate_min_price_per_km(3.00)
        self.assertTrue(True)


class MinDistanceValidatorTest(unittest.TestCase):

    def test_min_distance_validator_when_lower_value_should_raise(self):
        with self.assertRaises(ValidationError) as context:
            validate_min_distance(10)
        self.assertIsNotNone(context.exception)

    def test_min_distance_validator_when_correct_value_should_raise(self):

        validate_min_distance(100)
        self.assertTrue(True)

