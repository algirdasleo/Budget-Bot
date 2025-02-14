import os
from typing import List, Set, Tuple
import csv

from enums.CategoryEnum import CategoryEnum
from models.Payment import Payment
from models.Statistics import Statistics

KEYWORDS_FILE = "data/keywords.csv"
KEYWORDS_HEADERS = ["Category", "Keyword"]

def find_file(path: str) -> bool:
    """Checks file path"""
    return os.path.exists(path)


def check_headers(path: str, headers: List[str]) -> bool:
    """Validates file headers"""
    headers = set(headers)
    with open(path) as file:
        reader = csv.reader(file)
        try:
            file_headers = set(next(reader))
        except StopIteration:
            print(f"File headers are empty!\n")
            return False
        return headers.issubset(file_headers)
    

def load_payments(path: str) -> List[Payment]:
    """Loads user provided payments from CSV file"""
    
    headers = {"Description", "Payment Amount"}
    if not find_file(path):
        print(f"File '{path}' not found.")
        return []

    if not check_headers(path, headers):
        print(f"File '{path}' must have headers: {headers}.")
        return []    
    
    payments = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            description = row['Description']
            try:
                amount = float(row['Payment Amount'])
            except ValueError:
                print(f"Payment amount '{amount}' must be a number. Skipping...")
                continue
            if len(description) < 3:
                print(f"Description '{description}' must be at least 3 characters long. Skipping...")
                continue
            if float(amount) < 0:
                print(f"Payment amount '{amount}' cannot be negative. Skipping...")
                continue
            
            payments.append(Payment(description, amount))
            
    return payments


def create_file(file_name: str, headers: List[str]) -> None:
    """Creates a new file with headers"""
    if not find_file(file_name) or not check_headers(file_name, headers):
        with open(file_name, "w") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()


def load_keywords(name: str) -> List[str]:
    """Loads category keywords from CSV file"""
    category_keywords = []
    
    if not find_file(KEYWORDS_FILE):
        create_file(KEYWORDS_FILE, KEYWORDS_HEADERS)
        return category_keywords
    
    try:
        with open(KEYWORDS_FILE) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Category"] == name:
                    category_keywords.append(row["Keyword"])
                    
    except Exception as e:
        print(f"Error loading category keywords from '{KEYWORDS_FILE}': {e}")    
        
    return category_keywords


def add_keywords(data: List[Tuple[CategoryEnum, str]]) -> None:
    """Adds new category keywords to CSV file"""
    if not find_file(KEYWORDS_FILE):
        create_file(KEYWORDS_FILE, KEYWORDS_HEADERS)

    with open(KEYWORDS_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=KEYWORDS_HEADERS)

        # Write each new keyword to the file
        for category, keyword in data:
            writer.writerow({"Category": category.value, "Keyword": keyword})
            

def export_to_csv(stats: Statistics, file_name: str) -> None:
    """Exports categorized payments to CSV file"""
    file_name = "data/" + file_name
    headers = ["Description", "Payment Amount", "Category"]
    
    create_file(file_name, headers)
    with open(file_name, "a") as file:
        writer = csv.DictWriter(file, headers)
        for category, payment in stats.category_stats.items():
            for desc, amount in payment:
                writer.writerow({"Description": desc, "Payment Amount": amount, "Category": category.value})
        
    print(f"Successfully exported categorized payments to '{file_name}' file.")
