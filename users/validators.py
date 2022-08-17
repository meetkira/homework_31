from datetime import date

from django.core.exceptions import ValidationError


def check_email_validator(value: str):
    if 'rambler.ru' in value:
        raise ValidationError("Email can't contain 'rambler.ru'")

def check_age_validator(value: date):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 9:
        raise ValidationError("Age can't be less then 9")
