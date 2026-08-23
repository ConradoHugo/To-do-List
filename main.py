from variables import menu
from functions import create_new_list, create_new_task, edit_task, delete_task, delete_lists, view_all_list_and_keys

print("Welcome to the To-Do List")
print("Choose one of the following options:")

while menu == True:
    main_menu = input("""
1 To Create a new List
2 To Add a new task in your List
3 To Edit a task in your List
4 To Delete a task in your List
5 To Delete a list
6 To View all your lists and keys
7 To Exit
""")

    if main_menu == "1":
        create_new_list()

    if main_menu == "2":
        create_new_task()

    if main_menu == "3":
        edit_task()

    if main_menu == "4":
       delete_task()

    if main_menu == "5":
       delete_lists()

    if main_menu == "6":
       view_all_list_and_keys()

    if main_menu == "7":
        print("Leaving the Application")
        break


