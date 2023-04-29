"""Create unique filename.

Create unique filename.

Usage:
    from api.create_unique_filename import create_unique_filename

"""

from uuid import uuid4


def create_unique_filename(head: str) -> str:  # dead: disable
    """Create unique filename.

    Create unique filename.

    Argument:
       head: Head string

    Returns:
        A filename in the format {uuid}_{head}.wav

    """
    return f"{uuid4()}_{head}.wav"
