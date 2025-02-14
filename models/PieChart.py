import os
from typing import List
import matplotlib.pyplot as plt

class PieChart:
    """Represents a pie chart with labels and values"""
    def __init__(self, labels: List[str], values: List[int]):
        if len(labels) != len(values):
            raise ValueError("Invalid data for pychart: both labels and values must have the same length.")
        
        self.labels = labels
        self.values = values
    
    def display(self, description: str = None):
        """Displays a pie chart with the given data"""
        if not self.labels or not self.values:
            print("Error: Can not display PieChart with empty or none data.")
            return
        
        _, ax = plt.subplots(figsize=(6, 8))
        ax.set_position([0.17, 0.3, 0.7, 0.7])  # [left, bottom, width, height]  
        ax.pie(self.values, labels=self.labels, autopct='%1.1f%%', startangle=140)
        plt.title("Expenses Distribution")
        if description:
            plt.text(0, -1.9, description, ha='center', fontsize=12)
        plt.show(block=True)
        