from dataclasses import dataclass
from openai import OpenAI

from enums.CategoryEnum import CategoryEnum

@dataclass
class AICategorizer:
    def __init__(self, client: OpenAI):
        self.client = client
    
    def categorize(self, description: str) -> CategoryEnum:
        """Uses OpenAI API to categorize a payment"""
        prompt = "Classify this expense into one of these categories: "
        prompt += f"{', '.join([c.value for c in CategoryEnum])}. "
        prompt += f"Expense: {description}. Category: (just the name of the category)"
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a financial assistant that categorizes expenses."},
                        {"role": "user", "content": prompt}],
            max_tokens=5,
            temperature=0.0
    )
        
        category = response.choices[0].message.content
                
        for cat in CategoryEnum:
            if category.lower() == cat.value.lower():
                return cat
        
        return CategoryEnum.OTHER
    