# Adds tasks to a list
tasks = []
tasks.append("Study Python")
tasks.append("Exercise")
tasks.append("Read a Book")


# Removes a completed task
tasks.remove("Exercise")

# Displays tasks with numbers using enumerate()
for index , task in enumerate(tasks, start=1):
    print(index,tasks)
