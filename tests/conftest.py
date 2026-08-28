"""Test-wide guards.

One guard, and it exists because a property this repository relies on is
asserted in three documents and enforced by nothing: **the checks never touch
the network.** `workhouse.acquisition` fetches papers, `workhouse.oeis` fetches
the OEIS dump, and both keep that behind an explicit CLI flag — but nothing
stopped a future check from calling one of them, and a check that queried a
remote service would be run five to seven times per `make regen` plus once per
pytest run, would make `make catalogue` fail to reach a fixpoint the moment the
response changed, and would turn a recorded verdict into whatever the service
said today.

So the socket is closed for the duration of the suite. A test that genuinely
needs the network can ask for it with `@pytest.mark.network`, and the marker is
the visible record that it does.
"""

import socket

import pytest

_REAL_SOCKET = socket.socket


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "network: this test really does need the network (nothing does today)"
    )


class _Blocked(socket.socket):
    def __init__(self, *args, **kwargs):
        raise RuntimeError(
            "a test tried to open a socket. Nothing in the checks may touch the "
            "network: a verdict that depends on a remote service is not "
            "reproducible, and `make catalogue` would never reach a fixpoint. "
            "Pin the response and read the pin. If this test genuinely needs the "
            "network, mark it @pytest.mark.network."
        )


@pytest.fixture(autouse=True)
def _no_network(request):
    if request.node.get_closest_marker("network"):
        yield
        return
    socket.socket = _Blocked
    try:
        yield
    finally:
        socket.socket = _REAL_SOCKET
