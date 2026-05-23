# SPDX-FileCopyrightText: 2022 CERN.
# SPDX-License-Identifier: MIT

"""Test the requests record API."""


def test_grant_tokens(example_request):
    """Test if the expired system field works as intended."""
    data = example_request.dumps()
    assert data["grants"] == ["created_by.id.1", "receiver.id.2"]
