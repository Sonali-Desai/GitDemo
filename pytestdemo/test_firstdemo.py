#creating fixcture

import pytest


@pytest.fixture()
def fixdemo():
    print("I'll execute first")
    yield
    print("I'll execute Last")
def test_first():
    print("Hello")

@pytest.mark.smoke
def test_second():
    print("Hi")