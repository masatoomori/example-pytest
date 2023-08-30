from sample_pytest.module_1.prime import is_prime


def test_is_prime(is_prime_test_data):
    expected, input_value = is_prime_test_data
    assert is_prime(input_value) == expected
