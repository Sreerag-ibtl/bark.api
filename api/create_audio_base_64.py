"""Create audio base64.

Create audio base64.

Usage:
    from api.create_audio_base_64 import create_audio_base64

"""

from base64 import b64encode

from _io import TextIOWrapper


def create_audio_base_64(file: TextIOWrapper) -> str:  # dead: disable
    """Create audio base 64.

    Create audio base 64.

    Arguments:
        audio: Audio file object.

    Returns:
        Base64 string.

    """
    return b64encode(file.read()).decode("utf-8")
