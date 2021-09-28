from django.conf import settings


def calculate_total_value():
    """
    Calculates the sum from 1 to the max range.
    """
    numbers_to_add = list(range(settings.MAX_VALUE_TO_SUM + 1))
    return sum(numbers_to_add)
