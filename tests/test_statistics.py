import pytest
from models.Statistics import Statistics
from models.Payment import Payment
from enums.CategoryEnum import CategoryEnum

def test_update_statistics():
    stats = Statistics()
    payment = Payment("Grocery shopping", 50.0)
    
    stats.update(payment, CategoryEnum.SHOPPING)
    
    assert stats.category_stats[CategoryEnum.SHOPPING] == [("Grocery shopping", 50.0)]
    assert stats.total_spendings == 50.0

def test_negative_payment():
    stats = Statistics()
    
    with pytest.raises(ValueError, match="Payment amount cannot be negative."):
        stats.update(Payment("Invalid Payment", -10.0), CategoryEnum.OTHER)

def test_sort_statistics():
    stats = Statistics()
    
    stats.update(Payment("Lunch", 20.0), CategoryEnum.DINING)
    stats.update(Payment("Dinner", 40.0), CategoryEnum.DINING)
    stats.update(Payment("Transport Fee", 10.0), CategoryEnum.TRANSPORT)

    stats.sort()

    categories = list(stats.category_stats.keys())
    
    assert categories[0] == CategoryEnum.DINING
