from models.Payment import Payment


def get_menu_choice() -> str:
    """Displays menu options and returns user choice"""
    print("Please select a menu choice:")
    print("1. Open CSV file \n2. Enter payment information manually")
    print("3. Train Expense Categorizer\n")
    while True:
        choice = input("Menu choice: ")
        if choice not in ['1', '2', '3']:
            print("Invalid menu choice! Try entering '1', '2' or '3'\n")
            continue
        break
    return choice


def add_payment(i: int = 1) -> Payment:
    """Prompts user to enter payment information"""
    if i == 0:
        i = 1
    print(f"Payment {i}.")
    while True:
        try:
            description = input("Description: ").strip()
            if description == None:
                print("Please enter a valid description!\n")
                continue
            
            if len(description) < 3:
                print("Description must be at least 3 characters long!\n")
                continue
            
            if description.lower() == 'quit':
                return None
            
        except KeyboardInterrupt:
            return None
        break
            
    while True:
        try:
            amount_input = input("Payment Amount: ").strip()
            if amount_input.lower() == 'quit':
                return None
            amount = int(amount_input)
            if amount < 0:
                print("Payment amount cannot be negative!\n")
                continue
        except ValueError:
            print("Please enter a valid value!\n")
            continue
        except KeyboardInterrupt:
            return None
        break
    
    return Payment(description, amount)


def ai_insights() -> bool:
    """Prompts user to select an option of AI insights"""
    while True:
        choice = input("Would you like to get AI insights on your spending? (y/n): ").lower()
        if choice == 'y':
            print("AI insights selected!\n")
            break
        elif choice == 'n':
            print("No AI insights selected!\n")
            break
        else:
            print("Invalid choice! Please enter 'y' for yes or 'n' for no.\n")
            continue
        
    return choice == 'y'


def export_to_file() -> bool:
    """Prompts user to an option of exporting categorized payments to a file"""
    while True:
        choice = input("Would you like to export the categorized payments to a file? (y/n): ").lower()
        if choice == 'y':
            print("Exporting to file selected!\n")
            break
        elif choice == 'n':
            print("No export to file selected!\n")
            break
        else:
            print("Invalid choice! Please enter 'y' for yes or 'n' for no.\n")
            continue
        
    return choice == 'y'