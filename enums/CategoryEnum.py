from enum import Enum

class CategoryEnum(Enum):
    """Categories for expenses."""
    DINING = "Dining"
    TRANSPORT = "Transport"
    SHOPPING = "Shopping"
    ENTERTAINMENT = "Entertainment"
    UTILITIES = "Utilities"
    OTHER = "Other"