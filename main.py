import os
import sys
from typing import List
from dotenv import load_dotenv
from openai import OpenAI

from enums.CategoryEnum import CategoryEnum
from helpers import user_input_helper, file_helper

from models.AICategorizer import AICategorizer
from models.AIInsights import AIInsights
from models.ExpenseCategorizer import ExpenseCategorizer
from models.Payment import Payment
from models.PieChart import PieChart
from models.Statistics import Statistics


def init_openai_client() -> OpenAI:
    """Initializes OPENAI client and tests the API key"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Test the client
    try:
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Say Test"}],
            max_tokens=2,
            temperature=0.0
        )
    except Exception as e:
        sys.exit(f"Failed to initialize OpenAI client. Error code: {e}")
    
    return client


def get_user_payments() -> List[Payment]:
    """Handles the user's choice of adding payments and returns the list of payments"""
    while True:
        choice = user_input_helper.get_menu_choice()
        if choice == '1':
            payments = handle_file_choice()
        elif choice == '2':
            payments = handle_manual_choice()
        elif choice == '3':
            handle_training_choice()
            continue

        if choice in ['1', '2'] and len(payments) == 0:
            print("No payments were added! Please add payments before continuing.")
            continue
        break
    
    return payments


def handle_file_choice() -> List[Payment]:
    """Handles the user's choice of adding payments by CSV file"""
    print("Payments adding by CSV file selected!\n")
    
    print("Please enter the name of the CSV file in the 'Data' folder.")
    while True:
        file_name = input("File name: ")
        if not file_name:
            print("Please enter a valid file name!\n")
            continue
        path = './Data/' + file_name
        if not file_helper.find_file(path):
            print(f"File '{file_name}' does not exist in the 'Data' folder.")
            print("Please enter the file name correctly or add the file to 'Data' folder.\n")
            continue
        break
    
    headers = {'Description', 'Payment Amount'}
    if not file_helper.check_headers(path, headers):
        print("File must contain these columns with headers 'Description', 'Payment Amount'.\n")
        return []
        
    return file_helper.load_payments(path)


def handle_manual_choice() -> List[Payment]:
    """Handles the user's choice of adding payments manually"""
    print("Manual adding of payments selected!\n")
    print('Please add well-explained payment descriptions, f.e. "Coffee at Starbucks" for most accuracy.')
    print("In order to quit, type 'quit'.")
    
    payments = []
    while True:
        payment = user_input_helper.add_payment(len(payments) + 1)
        if payment is None:
            break
        payments.append(payment)
        print("Successfully added a new payment!\n")
    
    return payments


def handle_training_choice() -> None:
    """Handles the user's choice of training the Expense Categorizer"""
    print("Training of Expense Categorizer selected!\n")
    print("In order to quit, type 'quit'.")
    print("Please select New Words and Categories for the Expense Categorizer:")
    category_list = list(CategoryEnum)
    new_words = []
    
    while True:
        new_word = input("New word: ")
        if new_word.lower() == 'quit':
            break
        
        print("Category: ")
        for i, category in enumerate(category_list):
            print(f"{i + 1}. {category.value}")
            
        while True:
            try:
                category_choice = int(input("Category choice: ")) - 1
                if category_choice not in range(len(CategoryEnum)):
                    print("Invalid category choice! Please try again.")
                    continue
                selected_category = category_list[category_choice]
                new_words.append((selected_category, new_word))
                print(f"Successfully added '{new_word}' to the '{selected_category.value}' category!\n")
                break
            except ValueError:
                print("Invalid category choice! Please try again.")
                continue
            except KeyboardInterrupt:
                print("Exiting training...")
                return
    
    if len(new_words) == 0:
        print("No new words were added! Exiting training...\n")
        return
    
    print(f"Training complete! Successfully added {len(new_words)} new words to the Expense Categorizer.\n")
    file_helper.add_keywords(new_words)
    

def categorize_payments(payments: List[Payment], client: OpenAI) -> Statistics:
    """Categorizes the payments and returns the statistics"""
    ai_categorizer = AICategorizer(client)
    expense_categorizer = ExpenseCategorizer(ai_categorizer)
    statistics = Statistics()
    
    for payment in payments:
        category = expense_categorizer.categorize(payment.description)
        statistics.update(payment, category)
    
    return statistics
        

def display_statistics(statistics: Statistics, payments_count: int) -> None:
    """Displays the statistics and generates a pie chart"""
    statistics.sort()
    labels, values = statistics.get_chart_info()

    # Display a max of top 5 biggest payments
    if payments_count > 5:
        payments_count = 5
    
    top_payments = statistics.get_k_biggest_payments(payments_count)
    
    description = "Top Expenses by Amount spent:\n\n"
    description += "\n".join(
        f"{i + 1}. {cat}: '{desc}' - {amount}"
        for i, (cat, desc, amount) in enumerate(top_payments)
    )

    chart = PieChart(labels, values)
    chart.display(description)
    

def generate_ai_insights(statistics: Statistics, client: OpenAI) -> None:
    """Generates AI insights based on the statistics"""
    if not user_input_helper.ai_insights():
        return
    
    ai_insights = AIInsights(statistics, client)
    ai_insights.display_insights()
    

def export_to_file(statistics: Statistics) -> None:
    """Exports the categorized payments to a CSV file"""
    if not user_input_helper.export_to_file():
        return
    
    print("Please specify the name of the file to export the categorized payments.")
    while True:
        file_name = input("File name: ")
        if not file_name:
            print("Please enter a valid file name!")
            continue
        if not file_name.endswith(".csv"):
            print("File must end with .csv!")
            continue
        
        break
    
    file_helper.export_to_csv(statistics, file_name)


def main():
    load_dotenv()
    client = init_openai_client()
    
    print("Welcome to BudgetBot!")
    try:
        payments = get_user_payments()
        statistics = categorize_payments(payments, client)
        display_statistics(statistics, len(payments))
        generate_ai_insights(statistics, client)
        export_to_file(statistics)
    except KeyboardInterrupt:
        sys.exit("\nExiting BudgetBot...")
    
    print("Thank you for using BudgetBot! Goodbye!")

    
if __name__ == "__main__":
    main()