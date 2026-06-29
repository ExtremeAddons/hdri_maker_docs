"""
Utilities used by `conf.py` to provide dynamic metadata at build time.

This module exposes two functions (no try/except, no getattr/setattr):
- grab_release() -> str
- get_copyright() -> str

They are intentionally simple and assume the repository contains a valid
`exa_update.json` file in the project root (one level above the `docs` folder)
and that the JSON structure contains an "updates" mapping whose first key is
the current release string (insertion order is preserved in JSON files).

All code follows the project's constraints: no try/except and no dynamic
attribute access.
"""

import os
import json
import datetime


def _project_root():
    """Return the absolute path to the project root (parent of this `docs/`)."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def grab_release():
    """Read and return the release string from `exa_update.json`.

    Expected structure (example):
    {
        "updates": {
            "3.1.100": { ... },
            "3.0.121": { ... }
        }
    }

    This function returns the first key found inside the top-level
    `updates` mapping (file insertion order is preserved by Python's JSON loader).

    Note: per project rules no try/except is used; the file and keys must exist.
    """
    path = os.path.join(_project_root(), 'exa_update.json')
    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    updates = data['updates']
    # Return the first key from the mapping (insertion order)
    first_version = next(iter(updates))
    return first_version


def get_copyright():
    """Return the copyright string using the current year.

    Format: "{year}, Andrea Donati (Andrew_D)"
    """
    this_year = datetime.date.today().year
    return '{}, Andrea Donati (Andrew_D)'.format(this_year)

