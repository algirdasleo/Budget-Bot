from models.Statistics import Statistics
from openai import OpenAI

class AIInsights:
    def __init__(self, statistics: Statistics, client: OpenAI):
        self.statistics = statistics
        self.client = client
    
    def display_insights(self) -> None:
        """Uses OpenAI API to provide insights on user spending"""
        prompt = "Write 2 bullet points for what I should change or not change in my spending:\n"
        prompt += f"Total spendings: ${self.statistics.total_spendings}\n"
        prompt += "Category: Description - Amount\n"
        prompt += "\n".join(f"{category.value}: {desc} - ${amount}" 
                            for category, payments in self.statistics.category_stats.items() 
                            for desc, amount in payments)
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "You are a financial assistant that provides insights on spending."},
                            {"role": "user", "content": prompt}],
                max_tokens=150,
            )
            insights = response.choices[0].message.content
            print(f"AI Insights on Your Spending: \n {insights} \n")
        except Exception as e:
            print(f"Failed to get AI insights. Error code: {e}")
