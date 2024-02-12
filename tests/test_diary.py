from lib.diary import *

def test_returns_list_of_two_entries():
    diary = Diary("My title1", "one two three four five")
    diary = Diary("My title2", "six seven eight nine ten")
    assert diary.storage == [
        "My title1: one two three four five",
        "My title2", "six seven eight nine ten"
        ]