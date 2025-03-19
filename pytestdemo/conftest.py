import pytest


#@pytest.fixture(scope="class")
@pytest.fixture
def dataload():
    return ["abc","pqr","xyz"]

@pytest.fixture(params=["chrome","firefox","IE"])
def browsers(request):
    return request