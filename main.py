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

    def filter_by_priority(self, priority):
        """Return tasks filtered by priority level"""
        return [t for t in self.tasks if t.priority == priority]

    def remove(self, index):
        """Remove a task by index"""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)


# Usage
todo = TaskList()
todo.add("Write proposal", priority="high")
todo.add("Review PRs")
todo.add("Reply to emails", priority="low")
todo.add("Debug login issue", priority="high")

todo.complete(1)

print("All tasks:")
for task in todo.tasks:
    print(f"  {task}")

print("\nHigh priority tasks:")
for task in todo.filter_by_priority("high"):
    print(f"  {task}")

print(f"\nTotal: {len(todo.tasks)} | Pending: {len(todo.pending())}")

todo.remove(2)
print(f"After removal: {len(todo.tasks)} tasks")