import pytest

# is_prime_test_data is a fixture that returns a tuple of expected and input_value


@pytest.fixture(params=[
    (False, 1),
    (True, 2),
    (True, 3),
    (False, 4),
    (True, 5),
    (False, 6),
    (True, 7),
    (False, 8),
    (False, 9),
    (False, 10),
])
def is_prime_test_data(request):
    return request.param
