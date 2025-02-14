import pytest
from models.Payment import Payment

def test_payment_creation_valid():
    payment = Payment(description="Lunch at cafe", payment_amount=20.0)
    
    assert payment.description == "Lunch at cafe"
    assert payment.payment_amount == 20.0

def test_payment_negative_amount():
    with pytest.raises(ValueError, match="Payment amount cannot be negative."):
        Payment(description="Coffee", payment_amount=-5.0)

def test_payment_description_too_short():
    with pytest.raises(ValueError, match="Description must be at least 3 characters long."):
        Payment(description="A", payment_amount=10.0)

def test_payment_description_valid():
    payment = Payment(description="Coffee at Starbucks", payment_amount=5.0)
    
    assert payment.description == "Coffee at Starbucks"

    payment.description = "Lunch at restaurant"
    assert payment.description == "Lunch at restaurant"

def test_payment_amount_valid():
    payment = Payment(description="Dinner", payment_amount=30.0)
    
    assert payment.payment_amount == 30.0
    
    payment.payment_amount = 50.0
    assert payment.payment_amount == 50.0

def test_payment_amount_invalid():
    """Test that an exception is raised if we set a negative payment amount."""
    payment = Payment(description="Dinner", payment_amount=30.0)
    
    with pytest.raises(ValueError, match="Payment amount cannot be negative."):
        payment.payment_amount = -10.0
