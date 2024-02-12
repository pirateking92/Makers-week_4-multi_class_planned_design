Will contain the recipe inside here

# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem
    As a user
    So that I can record my experiences
    I want to keep a regular diary

    As a user
    So that I can reflect on my experiences
    I want to read my past diary entries

    As a user
    So that I can reflect on my experiences in my busy day
    I want to select diary entries to read based on how much time I have and my reading speed

    As a user
    So that I can keep track of my tasks
    I want to keep a todo list along with my diary

    As a user
    So that I can keep track of my contacts
    I want to see a list of all of the mobile phone numbers in all my diary entries

Some pointers:

    Remember that user stories don't map to classes 1:1. You'll need to digest the full problem and then develop a multi-class system that meets the user's needs.
    Don't worry about user interface or input-output. That means you shouldn't be using input() and only use print() for debugging purposes.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:

    def __init__(self):
        # passes empty list of entries from DiaryEntry
        pass # No code here yet

    def add(self, entry):
        # will add entries into the empty list above

    def all_entries(self):
        # will return all entries

    def count_words(self):
        # will count the number of words in the list and return it
        pass # No code here yet

    def reading_time(self, wpm):
        pass

    def find_best_entry_for_reading_time_given(self, wpm, minutes):
        pass

class DiaryEntry
    def __init__(self, title, contents):
        pass

    def format(self):
        pass

    def count_words(self):
class TodoList:

    def __init__(self):
        # will initialise an empty list
        pass # No code here yet

    def add_tasks(self, task_add):
        pass # No code here yet

    def mark_tasks_complete_and_remove(self, task_remove):
        pass

    def show_todo_list(self):
        # might not need to have this
        pass

class Contacts:
    def __init__(self):
        # initialise an empty contacts list of phone numbers. might need to be a dictionary
        pass
    def add_contacts_and_return(self)
        # will iterate through the diary(list) and search for phone number formatted numbers
        # will have to be given the correct format and such
        # remember that they don't need to be showed yet, we can just get them returned for our tests
        pass # No code here yet
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Small info at start to clarify. Diary and contacts will be the only classes directly working with each other
To do list is independent and will carry out actions on its own.
So integration tests should focus on diary and contacts. most likely it will be contacts just searching through the diary contents
"""
"""
given the whole Diary
When there are phone number formatted numbers in Diary
Return them to the contacts list
"""
contacts = Contacts()
entry_1 = Diary("title one", "one two 3 4 5")
entry_2 = Diary("title two", "six 07123456789")
entry_3 = Diary("title three", "space 07911111111 space")
contact.add_contacts_and_return() => ["07123456789", "07911111111"]

"""
add two diary entries
i see them back in the list
"""
def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "My contents 1")
    entry_2 = DiaryEntry("My title 2", "My contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
add two diary entries
and i call count words
i get the sum of all words in the contents of the diary entries
"""

def test_count_words_returns_count_of_all_words_in_all_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "one two three")
    entry_2 = DiaryEntry("My title 2", "four five six")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 6

"""
given i add two diary entries with a total length of 5
and a reading time of 2
then the total reading time should be 3
"""

def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "one two three")
    entry_2 = DiaryEntry("My title 2", "four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

"""
given a wpm of 1
and the amount of minutes to read as 5
return an entry with 5 words
"""

def test_reading_time_returns_suitable_entry_to_read():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "one two three four")
    entry_2 = DiaryEntry("My title 2", "one two three four five six seven")
    entry_3 = DiaryEntry("My title 2", "one two three four five six seven eight")
    entry_4 = DiaryEntry("My title 2", "one two three four five six seven eight nine")
    entry_5 = DiaryEntry("My title 2", "ten eleven twelve thirteen fourteen")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    diary.add(entry_5)
    assert diary.find_best_entry_for_reading_time(1, 5) == entry_5
"""
not sure how else the classes should interact with each other
"""

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE
class Diary

from lib.diary import Diary
"""
when i initialise with a title and contents
i can get back that title and content
"""

def test_constructs_and_get_title_and_contents():
    diary = Diary("My title", "My contents")
    assert diary.title == "My title"
    assert diary.contents == "My contents"

"""
when i initialise with five word contents
then count_words should return five
"""

def test_count_words_returns_word_count_of_contents():
    diary = Diary("My title", "My contents equals number five")
    assert diary.count_words() == 5

"""
given content of 6 words
wpm of 2
and minutes of 1
reading_chunk returns with the first four words
"""

def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary = Diary("My title", "one two three four five six")
    result = diary.reading_chunk(2, 1)
    assert result == "one two"

"""
Given a contents of six words
And a wpm of 2 and 1 minute
First time, reading_chunk returns "one two"
Next time, "three four"
"""
def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary = Diary("My title", "one two three four five six")
    assert diary.reading_chunk(2, 1) == "one two"
    assert diary.reading_chunk(2, 1) == "three four"



class Todo_List

from lib.todo_list import *

"""
empty list on initialise
"""
def test_empty_list_on_initialise():
    todo = ToDo()
    assert todo.todolist == []

"""
Given a task, 
will add to a list and show list to the user
"""

def test_to_add_to_list_and_return_it():
    todo = ToDo()
    todo.add_tasks("clean bedroom")
    assert todo.todolist == ["clean bedroom"]
# todo = ToDo()
# todo.add_tasks("clean bedroom")/
# assert todo.todolist == ["clean bedroom"]
    
def test_to_add_multiple_tasks_to_list():
    todo = ToDo()
    todo.add_tasks("clean bedroom")
    todo.add_tasks("clean kitchen")
    todo.add_tasks("clean toilet")
    assert todo.todolist == ["clean bedroom", "clean kitchen", "clean toilet"]

"""
Given a previous task,
remove from the list and show edited list to the user
"""
def test_remove_previous_entry():
    todo = ToDo()
    todo.add_tasks("clean bedroom")
    todo.add_tasks("clean kitchen")
    todo.add_tasks("clean toilet")
    todo.mark_tasks_complete_and_remove("clean kitchen")
    assert todo.todolist == ["clean bedroom", "clean toilet"]```

class Contacts

from lib.contacts import Contacts

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
