from api.v1.tools import calculate_total_value


def test_calculate_total_value(total_value):
    """
    Test case for total endpoint functionality.
    total_value: pytest fixture, coming from conftest.py
    """
    assert calculate_total_value() == total_value
