#List part 2

list = ["Cherry", "Banana", "Apple"]

def listmaker():
    while True:
        print("Menu:")
        print("add. Add a task to the to-do list")
        print("view. View the current to do list")
        print("mark as done. Mark a task as completed")
        print("remove. Remove a task from the to-do list")
        print("remove all. Remove all tasks from the to-do list")
        print("sort. Sort the list alphabetically")
        print("print numbers of to do list. Print the number of items on the To-do List")
        print("exit. Exit the program")

        action = input("Choose an option: ")

        if action == "add":
            addtolist = input("What would you like to add to the list? ")
            list.append(addtolist)
            print("Task added:", addtolist)

        elif action == "view":
            print("Current to-do list:")
            for item in list:
                print(item)

        elif action == "mark as done":
            markdone = input("Which item would you like marked as done? ")
            if markdone in list:
                i = list.index(markdone)
                list[i] = markdone + "☑"
                print("Task marked as done:", markdone)
            else:
                print("Task not found.")

        elif action == "remove":
            deletefromlist = input("What would you like to delete? ")
            if deletefromlist in list:
                list.remove(deletefromlist)
                print("Task removed:", deletefromlist)
            else:
                print("Task not found.")

        elif action == "remove all":
            list.clear()
            print("All tasks removed.")

        elif action == "sort":
            list.sort()
            print("List sorted alphabetically.")

        elif action == "print numbers of to do list":
            print("Number of items on the To-do List:", len(list))

        elif action == "exit":
            print("Leaving the program.")
            break

        else:
            print("Invalid option. Please choose an option between add, view, mark as done, remove, remove all, sort, print numbers of to do list, and exit.")

listmaker()
