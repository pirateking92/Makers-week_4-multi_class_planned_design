class Todo_List():
    
    def __init__(self):
        self.todo_list = []

    def add_tasks(self, task_add):
        return self.todo_list.append(task_add)
        # parameters:
        #   adding_tasks: (str) human readable text, may contain numbers, will be short sentences
        # return:
            # will add to a list, at first empty, and then containing multiple tasks
                # which will then be shown to the user
        pass
    def mark_tasks_complete_and_remove(self, task_remove):
        return self.todo_list.remove(task_remove)
        # parameters:
            # will search through the list to find and remove entries
        # return:
            # list with task entered, removed
        
    def show_reminder_list(self):
        # parameters:
            # will check the list
        # return:
            # the list with updated todo tasks
        pass