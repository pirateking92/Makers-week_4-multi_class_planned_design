from lib.diary_entry import *

def test_constructs_and_get_title_and_contents():
    diaryentry = DiaryEntry("My title", "My contents")
    assert diaryentry.title == "My title"
    assert diaryentry.contents == "My contents"

def test_count_words_returns_word_count_of_contents():
    diaryentry = DiaryEntry("My title", "My contents equals number five")
    assert diaryentry.count_words() == 5




