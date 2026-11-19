# 💰 Personal Expense Tracker with Data Visualization

## 📌 Project Overview

The **Personal Expense Tracker with Data Visualization** is a Python-based project designed to help users monitor their daily expenses, analyze spending patterns, and manage their budgets effectively.

The system stores expense records in CSV format, performs data cleaning and analysis, and generates meaningful visualizations and automated reports. It helps users understand where their money goes and make better financial decisions.

## 🎯 Project Objectives

- Track and manage personal expenses.
- Analyze spending patterns across different categories.
- Monitor monthly expenses.
- Compare spending against a predefined budget.
- Visualize financial data through charts.
- Generate automated expense reports.

## ✨ Key Features

- **Expense Tracking:** Add and store expenses using CSV files.
- **Data Cleaning:** Handle missing values, invalid amounts, and duplicate records.
- **Category Analysis:** Identify spending across food, transport, shopping, education, bills, and entertainment.
- **Monthly Analysis:** Understand monthly spending trends.
- **Payment Analysis:** Compare UPI, cash, and card transactions.
- **Budget Monitoring:** Compare expenses against a sample monthly budget of ₹15,000.
- **Data Visualization:** Generate four different charts.
- **Automated Reporting:** Create a text report containing expense analysis results.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| CSV | Expense data storage |

## 📁 Project Structure

```text
Personal-Expense-Tracker-Visualization/
│
├── data/
│   └── expenses.csv
│
├── notebooks/
│
├── src/
│   ├── data_manager.py
│   ├── analysis.py
│   ├── visualization.py
│   └── report.py
│
├── outputs/
│
├── images/
│   ├── category_expenses.png
│   ├── monthly_expenses.png
│   ├── payment_methods.png
│   └── expense_distribution.png
│
├── reports/
│   └── expense_report.txt
│
├── docs/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Personal-Expense-Tracker-Visualization.git
```

### 2. Navigate to the project folder

```bash
cd Personal-Expense-Tracker-Visualization
```

### 3. Create a virtual environment

```bash
py -3.11 -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install the required libraries

```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Project

Run the following command:

```bash
python main.py
```

The program automatically:

1. Creates a sample expense dataset if one does not exist.
2. Loads and cleans expense records.
3. Performs expense analysis.
4. Generates visualization charts.
5. Creates an automated expense report.

## ➕ Add a New Expense

To add a new expense manually