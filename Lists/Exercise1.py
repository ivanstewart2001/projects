to_do_list = []

while True:
    task = input("Enter a task for your to­-do list. Press <enter> when done: ")
    continue_user = input("Do you want to add another task? Yes/No: ")
    to_do_list.append(task)
    if continue_user == 'Yes':
        print("Task Added!")
        continue
    else:
        break

print()
print("Your to-do list: ")
print("-" * 16)
for task in to_do_list:
    print(task)