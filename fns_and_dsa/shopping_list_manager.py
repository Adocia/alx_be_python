shopping_list = []
while True:
    print("\n--- Shopping List Menu ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")

    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the shopping list.")
        else:
            print(f"'{item}' was not found in the shopping list.")

    elif choice == "3":
        print("\nYour Shopping List:")
        if len(shopping_list) == 0:
            print("The list is empty.")
        else:
            for i in shopping_list:
                print("-", i)

    elif choice == "4":
        print("Exiting... Goodbye!")
        break  

    
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
