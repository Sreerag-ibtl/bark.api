"""Test equality of two objects.

Test equality of two object.

Usage:
    python -m pytest -m tests/test_equality

"""

from base64 import b64decode, b64encode
from itertools import repeat
from os.path import exists
from typing import Any, Callable, List
from unittest import TestCase

import pytest
from fastapi import Response
from fastapi.testclient import TestClient

from api.create_audio_base_64 import create_audio_base_64
from api.create_unique_filename import create_unique_filename
from api.prediction import app
from api.remove_file import remove_file

# Prepare test case.
test_case: TestCase = TestCase()

# Prepare FastAPI test client.
fast_api_client: TestClient = TestClient(app)

# Call /predict
response: Response = fast_api_client.get("/predict/?prompt=a cello tune")

# Get audio as byte string.
audio_base_64: str = response.json()["audio_base_64"]

# Decode and check has RIFF in string.
decoded_audio_has_riff: bool = audio_base_64.__contains__("RIFF")

# Create unique filename.
unique_filenames: List[str] = list(
    map(create_unique_filename, repeat("a cello tune", 100))
)

# Create an empty file.
open("empty_file", "wb").close()

# Remove file.
remove_file("empty_file")

# Create file for testing create_audio_base_64.
open("file_for_testing_create_audio_base_64", "wb").close()  # ...........
file_for_testing_create_audio_base_64 = open(
    "file_for_testing_create_audio_base_64", "rb"
)

# Convert to base64.
base_64: str = create_audio_base_64(file_for_testing_create_audio_base_64)

# Decode and encode back.
decode_encode_audio_base_64: str = b64encode(b64decode(base_64)).decode(
    "utf-8"
)  # ................

# Close file object.
file_for_testing_create_audio_base_64.close()

# Remove file.
remove_file("file_for_testing_create_audio_base_64")


@pytest.mark.parametrize(
    "lhs, rhs, assert_equality",
    (
        (response.status_code, 200, test_case.assertEqual),
        (decoded_audio_has_riff, True, test_case.assertEqual),
        (len(set(unique_filenames)), 100, test_case.assertEqual),
        (exists("empty_file"), False, test_case.assertEqual),
        (decode_encode_audio_base_64, audio_base_64, test_case.assertEqual),
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
