import pytest
from models.ExpenseCategorizer import ExpenseCategorizer
from enums.CategoryEnum import CategoryEnum

class MockAICategorizer:
    def categorize(self, description) -> CategoryEnum:
        return CategoryEnum.OTHER

def test_expense_categorizer():
    ai_categorizer = MockAICategorizer()
    expense_categorizer = ExpenseCategorizer(ai_categorizer)

    # DINING
    assert expense_categorizer.categorize("McDonalds") == CategoryEnum.DINING
    assert expense_categorizer.categorize("KFC") == CategoryEnum.DINING
    assert expense_categorizer.categorize("Starbucks Coffee") == CategoryEnum.DINING
    assert expense_categorizer.categorize("Burger King") == CategoryEnum.DINING
    assert expense_categorizer.categorize("Taco Bell") == CategoryEnum.DINING

    # TRANSPORT
    assert expense_categorizer.categorize("Uber ride") == CategoryEnum.TRANSPORT
    assert expense_categorizer.categorize("Lyft trip") == CategoryEnum.TRANSPORT
    assert expense_categorizer.categorize("Gas Station") == CategoryEnum.TRANSPORT
    assert expense_categorizer.categorize("MetroCard top-up") == CategoryEnum.TRANSPORT
    assert expense_categorizer.categorize("Train Ticket") == CategoryEnum.TRANSPORT

    # SHOPPING
    assert expense_categorizer.categorize("Amazon purchase") == CategoryEnum.SHOPPING
    assert expense_categorizer.categorize("Nike sneakers") == CategoryEnum.SHOPPING
    assert expense_categorizer.categorize("Walmart groceries") == CategoryEnum.SHOPPING
    assert expense_categorizer.categorize("Best Buy electronics") == CategoryEnum.SHOPPING
    assert expense_categorizer.categorize("Target items") == CategoryEnum.SHOPPING

    # ENTERTAINMENT
    assert expense_categorizer.categorize("Netflix subscription") == CategoryEnum.ENTERTAINMENT
    assert expense_categorizer.categorize("Spotify music") == CategoryEnum.ENTERTAINMENT
    assert expense_categorizer.categorize("Hulu show") == CategoryEnum.ENTERTAINMENT
    assert expense_categorizer.categorize("Disney+ subscription") == CategoryEnum.ENTERTAINMENT
    assert expense_categorizer.categorize("Concert Tickets") == CategoryEnum.ENTERTAINMENT

    # UTILITIES
    assert expense_categorizer.categorize("Electric Bill payment") == CategoryEnum.UTILITIES
    assert expense_categorizer.categorize("Water Bill payment") == CategoryEnum.UTILITIES
    assert expense_categorizer.categorize("Internet payment") == CategoryEnum.UTILITIES
    assert expense_categorizer.categorize("Phone Bill payment") == CategoryEnum.UTILITIES
    assert expense_categorizer.categorize("Gas Bill payment") == CategoryEnum.UTILITIES

    # OTHER (Default category)
    assert expense_categorizer.categorize("Random stuff") == CategoryEnum.OTHER
    assert expense_categorizer.categorize("Unknown category item") == CategoryEnum.OTHER

