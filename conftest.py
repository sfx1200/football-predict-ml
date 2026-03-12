"""Root conftest — runs before any test collection/import."""
from pathlib import Path


def pytest_configure(config):
    """Create required directories before modules are imported."""
    for d in ("logs", "data/raw", "data/processed", "models"):
        Path(d).mkdir(parents=True, exist_ok=True)
