from unittest.mock import patch

import pytest


@pytest.fixture(scope="session", autouse=True)
def mock_input():
    """Provides mocked input for python built in input
    mock_input can be reused across tests"""
    with patch("builtins.input") as mocked_input:
        yield mocked_input
