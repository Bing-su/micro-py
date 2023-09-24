from importlib.metadata import version

try:
    __version__ = version(__name__)
except Exception:
    __version__ = "0.0.0"
