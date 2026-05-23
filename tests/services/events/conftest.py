# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 TU Wien.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-License-Identifier: MIT

"""Request Events conftest."""

import pytest

from invenio_requests.customizations.event_types import CommentEventType, LogEventType
from invenio_requests.records.api import RequestEventFormat


@pytest.fixture()
def events_service_data():
    """Input data for the Request Events Service."""
    return dict(
        comment={
            "type": CommentEventType.type_id,
            "payload": {
                "content": "This is a comment.",
                "format": RequestEventFormat.HTML.value,
            },
        },
        log={
            "type": LogEventType.type_id,
            "payload": {
                "content": "This is a log event.",
                "format": RequestEventFormat.HTML.value,
                "event": "LOG_EVENT",
            },
        },
    )
