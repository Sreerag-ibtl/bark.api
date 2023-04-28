"""Test equality of two objects.

Test equality of two object.

Usage:
    python -m pytest -m tests/test_equality

"""

from typing import Any, Callable


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
