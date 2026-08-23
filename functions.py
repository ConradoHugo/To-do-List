from variables import to_do_list, menu

#1 To Create a new List
#2 To Add a new task in your List
#3 To Edit a task in your List
#4 To Delete a task in your List
#5 To View all your Tasks
#6 To View all your lists
#6 To Exit

def create_new_list():
    while True:
            name_list = input("What the name of the new list?")
            if name_list in to_do_list:
                print("This list is already there")
                continue
            to_do_list[name_list] = []
            print(f"The name of the new list is: {to_do_list.keys()}" )
            option = input("Want to continue? (y/n):").lower()
            if option == "y":
                continue
            if option == "n":
                print("Ok returning to the main menu")
                menu
                break
            else:
                print("Invalid, please use Y or N")
                continue

def create_new_task():
    while True:
        task_name = input("What the name of the new task?")

        print(f"Possible lists for put your task: {to_do_list.keys()}")
        list_name = input("Where list you want put your task?")
        if list_name not in to_do_list.keys():
            print(f"The list {list_name} doesn't exist")
            continue
        to_do_list[list_name].append(task_name)

        option = input("Want to continue? (y/n):").lower()
        if option == "y":
            continue
        if option == "n":
            print("Ok returning to the main menu")
            menu
            break
        else:
            print("Invalid, please use Y or N")
            continue

def edit_task():
    while True:
        print(f"Choose a lists and after that choose a task to edit: {to_do_list.keys()}")
        list_name = input("Which list do you want to edit?")
        if list_name not in to_do_list.keys():
            print(f"The list {list_name} doesn't exist")
            continue
        print(f"Possible tasks to edit in the list: {to_do_list[list_name]}")
        ed_task = input("What would you like to edit?")
        if ed_task not in to_do_list[list_name]:
            print("That task does not exist")
            continue
        new_name_task = input("What would you like to do now?")
        index_task = to_do_list[list_name].index(ed_task)
        to_do_list[list_name][index_task] = new_name_task
        print(f"Now this is your new task: {to_do_list[list_name][index_task]} in the list: {to_do_list[list_name]}")

        option = input("Want to continue? (y/n):").lower()
        if option == "y":
            continue
        if option == "n":
            print("Ok returning to the main menu")
            menu
            break
        else:
            print("Invalid, please use Y or N")
            continue

def delete_task():
    while True:
        print(f"Choose a lists and after that choose a task to delete: {to_do_list.keys()}")
        list_name = input("Which list do you want to delete a task from?")
        if list_name not in to_do_list.keys():
            print(f"The list {list_name} doesn't exist")
            continue
        print(f"Possible tasks to delete in the list: {to_do_list[list_name]}")
        del_task = input("What would you like to delete?")
        if del_task not in to_do_list[list_name]:
            print("That task does not exist")
            continue
        index_task = to_do_list[list_name].index(del_task)
        to_do_list[list_name].pop(index_task)
        print(f"Now this is yours remainders task: {to_do_list[list_name]} in the list:")

        option = input("Want to continue? (y/n):").lower()
        if option == "y":
            continue
        if option == "n":
            print("Ok returning to the main menu")
            menu
            break
        else:
            print("Invalid, please use Y or N")
            continue

def delete_lists():
    while True:
        print(f"Choose a lists to delete: {to_do_list.keys()}")
        del_list = input("Which list do you want to delete: ")
        if del_list not in to_do_list:
            print(f"The list {del_list} doesn't exist")
            continue
        del to_do_list[del_list]
        print(f"Now this is yours remainders list: {to_do_list}")

        option = input("Want to continue? (y/n):").lower()
        if option == "y":
            continue
        if option == "n":
            print("Ok returning to the main menu")
            menu
            break
        else:
            print("Invalid, please use Y or N")
            continue

def view_all_list_and_keys():
        print(to_do_list)
