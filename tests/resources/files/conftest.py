# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-License-Identifier: MIT

"""Request Files Resource conftest."""

import pytest

from invenio_requests.records.api import RequestEventFormat


@pytest.fixture()
def headers_upload():
    """Default headers for uploads."""
    return {
        "content-type": "application/octet-stream",
        "accept": "application/json",
    }


@pytest.fixture()
def events_resource_data():
    """Input data for the Request Events Resource (REST body)."""
    return {
        "payload": {
            "content": "This is a comment.",
            "format": RequestEventFormat.HTML.value,
        }
    }
