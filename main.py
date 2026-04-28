# Example: A simple task tracker

class Task:
    def __init__(self, title, priority="medium"):
        self.title = title
        self.priority = priority
        self.done = False

    def complete(self):
        self.done = True

    def __repr__(self):
        status = "✓" if self.done else "○"
        return f"{status} [{self.priority}] {self.title}"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, title, priority="medium"):
        self.tasks.append(Task(title, priority))

    def complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()

    def pending(self):
        return [t for t in self.tasks if not t.done]


# Usage
todo = TaskList()
todo.add("Write proposal", priority="high")
todo.add("Review PRs")
todo.add("Reply to emails", priority="low")

todo.complete(1)

for task in todo.tasks:
    print(task)

print(f"\n{len(todo.pending())} task(s) remaining")