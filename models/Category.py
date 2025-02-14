from dataclasses import dataclass
from typing import Set
from enums.CategoryEnum import CategoryEnum
from helpers.file_helper import load_keywords

@dataclass
class Category:
    """Represents a category with a name and keywords"""
    name: CategoryEnum
    keywords: Set[str]

    def __init__(self, name: CategoryEnum):
        """Initializes a category with a name and loads keywords from file"""
        self.name = name
        self.keywords = set()
        try:
            self.keywords.update(load_keywords(name.value))
        except Exception as e:
            print(f"Error loading keywords for category '{name}': {e}")
            