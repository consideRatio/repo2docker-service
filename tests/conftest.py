import asyncio

import pytest


@pytest.fixture(scope="module")
def event_loop(request):
    """Create an instance of the default event loop for each test module as
    compared to each test case which is the default with pytest_asyncio."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
