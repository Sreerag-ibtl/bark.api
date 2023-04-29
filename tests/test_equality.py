"""Test equality of two objects.

Test equality of two object.

Usage:
    python -m pytest -m tests/test_equality

"""

from base64 import b64decode
from itertools import repeat
from typing import Any, Callable, List
from unittest import TestCase

import pytest
from fastapi import Response
from fastapi.testclient import TestClient

from api.create_unique_filename import create_unique_filename
from api.prediction import app

# Prepare test case.
test_case: TestCase = TestCase()

# Prepare FastAPI test client.
fast_api_client: TestClient = TestClient(app)

# Call /predict
response: Response = fast_api_client.get("/predict/?prompt=a cello tune")

# Get audio as byte string.
audio_base_64: str = response.json()["audio_base_64"]

# Decode and check has RIFF in string.
decoded_audio_base_64: str = b64decode(audio_base_64).decode("utf-8")
decoded_audio_has_riff: bool = decoded_audio_base_64.__contains__("RIFF")

# Create unique filename.
unique_filenames: List[str] = list(
    map(create_unique_filename, repeat("a cello tune", 100))
)


@pytest.mark.parametrize(
    "lhs, rhs, assert_equality",
    (
        (response.status_code, 200, test_case.assertEqual),
        (decoded_audio_has_riff, True, test_case.assertEqual),
        (len(set(unique_filenames)), 100, test_case.assertEqual),
    ),  # ............
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
