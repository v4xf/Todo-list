
def view_list(MyList):
    if not MyList:
        print("\nList is empty 😕")
    else:
        print("\nList: 📄")
        for Num, tsk in enumerate(MyList, start=1):
            print(f"{Num}. {tsk}")



def add_task(MyList):
    newtsk = input("\nEnter a new task:  ")
    MyList.append(newtsk)
    print(f"'{newtsk}' has been added the list ✅")



def remove_task(MyList):
    view_list(MyList)
    if MyList:
        try:
            N = int(input("\nEnter the number of task to remove: "))
            if 1 <= N <= len(MyList):
                N2 = N-1
                MyList.pop(N2)
                print(f"'{N2}' has been removed from your to-do list ✅")
            else:
                print("Invalid number ❌")
        except ValueError:
            print("Please enter a valid number.")



def main():
    MyList = []
    print("\n------WELCOME------")
    while True:
        print("===================")
        print("1. View To-Do List 🔍")
        print("2. Add a task ✏️")
        print("3. Remove a task 📤")
        print("4. Exit 🚪")
        inpt = input("Choose an option: ")
        
        if inpt == "1":
            view_list(MyList)
        elif inpt == "2":
            add_task(MyList)
        elif inpt == "3":
            remove_task(MyList)
        elif inpt == "4":
            print("👋😀")
            break
        else:
            print(f"\n'{inpt}'is not an option ❌\n Please select a valid option.")



main()
