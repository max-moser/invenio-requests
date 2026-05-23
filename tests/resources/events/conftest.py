# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 TU Wien.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-License-Identifier: MIT

"""Request Events Resource conftest."""

import pytest

from invenio_requests.records.api import RequestEventFormat


@pytest.fixture()
def events_resource_data():
    """Input data for the Request Events Resource (REST body)."""
    return {
        "payload": {
            "content": "This is a comment.",
            "format": RequestEventFormat.HTML.value,
        }
    }
