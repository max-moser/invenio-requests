# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-License-Identifier: MIT

"""Module tests."""

from flask import Flask

from invenio_requests import InvenioRequests


def test_version():
    """Test version import."""
    from invenio_requests import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioRequests(app)
    assert "invenio-requests" in app.extensions

    app = Flask("testapp")
    ext = InvenioRequests()
    assert "invenio-requests" not in app.extensions
    ext.init_app(app)
    assert "invenio-requests" in app.extensions
