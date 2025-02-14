# BudgetBot

## Description

BudgetBot is a personal finance tool that helps users categorize their expenses, generate insights, and visualize spending patterns. It leverages a set-based manual categorizer and OpenAI's GPT-4 as back-up to classify payments into predefined categories. The app supports manual entry, CSV file uploads, and training the categorizer with custom keywords.

## Features

- **Categorize Payments**: Automatically categorize payments based on descriptions using the AI-powered Expense Categorizer.
- **CSV Upload**: Load payments from CSV files to categorize them quickly.
- **Manual Entry**: Add payments manually and categorize them with the AI categorizer.
- **Training Mode**: Train the categorizer with new keywords and categories for better accuracy.
- **AI Insights**: Generate insights and suggestions on spending habits.
- **Pie Chart Visualization**: View spending distribution in a pie chart format.
- **Export Data**: Export categorized payment data to a CSV file for further analysis.

## Installation

### Prerequisites

1. Python 3.xx
2. OpenAI API Key
3. Libraries required:
   - `openai`
   - `python-dotenv`
   - `matplotlib` (for generating pie charts)

### Setup

1. Clone the repository

2. Navigate to the project folder:
   ```bash
   cd budgetbot
   ```
3. Install the required dependencies:

   ```bash
   pip install openai python-dotenv matplotlib pytest
   ```

4. Create a `.env` file at the root of the project and add your OpenAI API Key:

   ```bash
   OPENAI_API_KEY=your-openai-api-key-here
   ```

5. Create a `data` folder in the root directory where CSV files will be stored.

## Usage

### Starting the Application

Run the application using the following command:

```bash
python main.py
```

### Example CSV Format

To upload payments via CSV, ensure the file contains the following columns:

```csv
Description,Payment Amount
Coffee at Starbucks,5.50
Groceries at Walmart,30.00
```
