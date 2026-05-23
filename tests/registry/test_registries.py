# SPDX-FileCopyrightText: 2025 CESNET i.a.l.e.
# SPDX-License-Identifier: MIT

"""Test for entrypoint loading."""

from tests.mock_module import MockEventType, MockRequestType, MockResolver


def test_request_type_registry_entrypoints(app):
    registry = app.extensions["invenio-requests"].request_type_registry
    assert isinstance(registry.lookup("mock"), MockRequestType)


def test_event_type_registry_entrypoints(app):
    registry = app.extensions["invenio-requests"].event_type_registry
    assert isinstance(registry.lookup("M"), MockEventType)


def test_entity_resolvers_registry_entrypoints(app):
    registry = app.extensions["invenio-requests"].entity_resolvers_registry
    assert isinstance(registry.lookup("mock"), MockResolver)
