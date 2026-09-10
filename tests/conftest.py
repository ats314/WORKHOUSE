from __future__ import annotations

import os
import tempfile


def pytest_configure(config) -> None:
    """Ensure pytest basetemp is accessible.

    On Windows workstations, an inaccessible %TEMP%/pytest-of-<user> directory
    (e.g. created by elevated or foreign service accounts) causes PermissionError
    when scanning for numbered directories. Fall back to a repository-local
    temporary root if the default temp directory is unreadable.
    """
    if not config.option.basetemp:
        try:
            user = os.environ.get("USERNAME") or os.environ.get("USER") or "user"
            temp_root = os.path.join(tempfile.gettempdir(), f"pytest-of-{user}")
            if os.path.exists(temp_root):
                list(os.scandir(temp_root))
        except (OSError, PermissionError):
            repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            safe_temp = os.path.join(repo_root, ".pytest_temp")
            os.makedirs(safe_temp, exist_ok=True)
            config.option.basetemp = safe_temp
