class Payment:
    """Represents a payment with a description and payment amount"""
    
    def __init__(self, description: str, payment_amount: float):
        self.description = description
        self.payment_amount = payment_amount

    @property
    def payment_amount(self) -> float:
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value: float):
        if value < 0:
            raise ValueError("Payment amount cannot be negative.")
        self._payment_amount = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        if len(value) < 3:
            raise ValueError("Description must be at least 3 characters long.")
        self._description = value
