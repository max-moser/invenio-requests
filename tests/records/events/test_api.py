# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-FileCopyrightText: 2021 TU Wien.
# SPDX-License-Identifier: MIT

import pytest
from jsonschema import ValidationError

from invenio_requests.customizations.event_types import CommentEventType
from invenio_requests.records import RequestEvent


def test_request_event_jsonschema(app, db, example_request):
    event = RequestEvent.create(
        {},
        request=example_request.model,
        request_id=example_request.number,
        type=CommentEventType,
    )
    db.session.commit()
    assert event.schema

    # JSONSchema validation works.
    with pytest.raises(ValidationError):
        RequestEvent.create(
            {"garbage": {"bar": 1}},
            request=example_request.model,
            request_id=example_request.number,
            type=CommentEventType,
        )
