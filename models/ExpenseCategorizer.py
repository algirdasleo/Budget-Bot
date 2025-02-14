from dataclasses import dataclass
from typing import List
from enums.CategoryEnum import CategoryEnum
from models.AICategorizer import AICategorizer
from models.Category import Category

@dataclass
class ExpenseCategorizer:
    categories: List[Category]
    ai_categorizer: AICategorizer
    
    def __init__(self, ai_categorizer: AICategorizer):
        """Initializes a list of categories and an AI categorizer as backup"""
        self.categories = [Category(name) for name in CategoryEnum]
        self.ai_categorizer = ai_categorizer
        
    def categorize(self, description: str) -> CategoryEnum:
        """Categorizes an expense based on keywords"""
        description = description.lower()
        
        for category in self.categories:
            if any(keyword.lower() in description for keyword in category.keywords):
                return category.name
        
        # Use AI as backup
        return self.ai_categorizer.categorize(description)
    