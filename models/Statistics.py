from dataclasses import dataclass
from typing import Dict, List, Tuple

from enums.CategoryEnum import CategoryEnum
from models.Payment import Payment

@dataclass
class Statistics:
    """Represents the statistics of payments"""
    category_stats: Dict[CategoryEnum, List[Tuple[str, float]]] = None
    
    def __init__(self):
        self.category_stats = {}
        self.total_spendings = 0.0 
    
    def update(self, payment: Payment, category_name: CategoryEnum):
        """Update the statistics with a new payment"""
        if payment.payment_amount < 0:
            raise ValueError("Payment amount cannot be negative.")
        if len(payment.description) < 3:
            raise ValueError("Description must be at least 3 characters long.")
        
        if category_name in self.category_stats:
            self.category_stats[category_name].append((payment.description, payment.payment_amount))
        else:
            self.category_stats[category_name] = [(payment.description, payment.payment_amount)]
        self.total_spendings += payment.payment_amount
        
    def sort(self):
        """Sort the categories by payment amount decreasingly"""
        self.category_stats = dict(
            sorted(
                self.category_stats.items(), 
                key=lambda stat: sum(amount for _, amount in stat[1]), 
                reverse=True
            )
        )
    
    def get_chart_info(self) -> Tuple[List[str], List[float]]:
        """Returns category names and sum of all payments for that category"""
        labels = [category.value for category in self.category_stats]
        values = [
            sum(amount for _, amount in payments)
            for payments in self.category_stats.values()
        ]
        
        return labels, values
    
    def get_k_biggest_payments(self, k: int) -> List[Tuple[str, str, float]]:
        """Returns the k biggest payments"""
        all_payments = [
            (category.value, desc, amount)
            for category, payments in self.category_stats.items()
            for desc, amount in payments
        ]
        
        return sorted(all_payments, key=lambda x: x[2], reverse=True)[:k]
    
    @property
    def total_spendings(self) -> float:
        return self._total_spendings

    @total_spendings.setter
    def total_spendings(self, value: float):
        if value < 0:
            raise ValueError("Total spendings cannot be negative.")
        self._total_spendings = value
        