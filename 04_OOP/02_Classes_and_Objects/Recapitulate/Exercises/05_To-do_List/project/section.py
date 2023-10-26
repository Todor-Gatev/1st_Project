from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []
        self.completed_tasks = set()

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for task_n in self.tasks:
            if task_n.name == task_name:
                task_n.completed = True
                self.completed_tasks.add(task_n)

                return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        removed_tasks = len(self.completed_tasks)

        self.tasks = list(self.completed_tasks.symmetric_difference(self.tasks))

        return f"Cleared {removed_tasks} tasks."

    def view_section(self) -> str:
        return f"Section {self.name}:\n" + "\n".join(t.details() for t in self.tasks)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

section.complete_task(second_task.name)
print(section.clean_section())
print(section.view_section())
