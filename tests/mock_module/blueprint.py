# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-License-Identifier: MIT

"""Blueprint of Mock Module."""

from flask import Blueprint


def create_ui_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "invenio_requests_mock_module",
        __name__,
    )

    @blueprint.route("/requests/<request_pid_value>")
    def request_detail(id):
        return "fake detail page"

    return blueprint
