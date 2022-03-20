import os
import pathlib

__version__ = "Unknown"

_pkg_dir = pathlib.Path(os.path.dirname(__file__))
_version_file = _pkg_dir.parent / "version.txt"
if os.path.exists(_version_file):
    with open(_version_file, "rt") as fo:
        __version__ = fo.read().strip()
