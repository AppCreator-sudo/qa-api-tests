import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL