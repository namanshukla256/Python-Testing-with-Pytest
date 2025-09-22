from cards import Card
import pytest

# Helper function to assert that two Card objects are identical (Assertion helper function)
def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True # Hide this function from tracebacks
    assert c1 == c2
    if c1.id != c2.id:
        pytest.fail(f"IDs differ: {c1.id} != {c2.id}")

def test_identical():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=123)
    assert_identical(c1, c2) # This should pass

def test_not_identical():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=456)
    assert_identical(c1, c2) # This should fail with a clear message