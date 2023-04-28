"""Test equality of two objects.

Test equality of two object.

Usage:
    python -m pytest -m tests/test_equality

"""

from typing import Any, Callable
from unittest import TestCase

import pytest
from api.prediction import app
from fastapi import Response
from fastapi.testclient import TestClient

# Prepare test case.
test_case: TestCase = TestCase()

# Prepare FastAPI test client.
fast_api_client: TestClient = TestClient(app)

# Call /predict
response: Response = fast_api_client.get("/predict/?prompt=a cello tune")


@pytest.mark.parametrize(
    "lhs, rhs, assert_equality",
    ((response.status_code, "200", test_case.assertEqual),),  # ............
)
def test_equality(
    lhs: Any, rhs: Any, assert_equality: Callable[[Any, Any], None]
) -> None:
    """Test equality of two objects.

    Test the equality of the two objects.

    Arguments:
        lhs: Left hand side of the equality.
        rhs: Right hand side of the equality.
        assert_equality: A function that assert equality.

    Returns:
        None

    Raises:
        AssertionError

    """
    assert_equality(lhs, rhs)
