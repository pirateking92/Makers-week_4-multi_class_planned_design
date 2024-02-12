from math import ceil

class DiaryEntry:

    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary must have a title or contents")
        self.title = title
        self.contents = contents
        self.read_so_far = 0
    
    def format(self):
        pass

    def count_words(self):
        pass