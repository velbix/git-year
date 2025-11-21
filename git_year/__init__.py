from importlib import metadata

try:
    __version__ = metadata.version("git-year")
except metadata.PackageNotFoundError:
    __version__ = "unknown (metadata unavailable)"
