def display_menu():
    print("Shopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")

        elif choice == '2':
            item = ("Enter the item to remove: ")
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
            
        elif choice == '3':
            print("Current shopping list:", shopping_list)
            
        elif choice == '4':
            print("Good bye!")
            break
        else:
            print("Invalid choice. Please try again")

main()