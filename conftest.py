import pytest
from django.conf import settings


@pytest.fixture
def total_value():
    return sum(range(settings.MAX_VALUE_TO_SUM + 1))
