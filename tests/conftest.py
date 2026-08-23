# TODO: Validate
import pytest
from get_around import build_client_automatically

from plugi import Plugi


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> Plugi:
    return Plugi(build_client_automatically())
