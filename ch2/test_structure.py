import pytest, cards
from cards import Card

def test_to_dict():
    # GIVEN a Card object with known contents
    c1 = Card("something", "brian", "todo", 123)

    # WHEN we convert it to a dictionary
    c2 = c1.to_dict()

    # THEN the dictionary should have the expected contents
    c2_expected = {
        "summary": "something",
        "owner": "brian",
        "status": "todo",
        "id": 123
    }

    assert c2 == c2_expected