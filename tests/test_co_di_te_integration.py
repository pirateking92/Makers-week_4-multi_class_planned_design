from lib.contacts import *
from lib.diary import *
from lib.todo_list import *

def test_returns_list_of_two_entries():
    diary = Diary("My title1", "one two three four five")
    diary = Diary("My title2", "six seven eight nine ten")
    assert diary.storage == [
        "My title1: one two three four five",
        "My title2", "six seven eight nine ten"
        ]

"""
given the whole Diary
When there are phone number formatted numbers in Diary
Return them to the contacts list
"""
# contacts = Contacts()
# entry_1 = Diary("title one", "one two 3 4 5")
# entry_2 = Diary("title two", "six 07123456789")
# entry_3 = Diary("title three", "space 07911111111 space")
# contact.add_contacts_and_return() => ["07123456789", "07911111111"]