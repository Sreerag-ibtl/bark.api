"""remove_file.

Remove file.

Usage:
    from api.remove_file import remove_file

"""

from os import remove


def remove_file(filename: str) -> None:
    """Remove file.

    Remove file.

    Arguments:
        filename: Filename to remove.

    Returns:
        None

    """
    remove(filename)
