
import argparse

from src.data_manager import load_expenses, add_expense
from src.analysis import (
    calculate_summary,
    category_analysis,
    monthly_analysis,
    payment_analysis,
    budget_analysis
)
from src.visualization import create_visualizations
from src.report import generate_report


def run_project():

    print("\n======================================")
    print("   PERSONAL EXPENSE TRACKER")
    print("   WITH DATA VISUALIZATION")
    print("======================================")

    # Load expense dataset
    df = load_expenses()

    print(f"\nSuccessfully loaded {len(df)} expense records.")

    # Perform expense analysis
    summary = calculate_summary(df)
    category_totals = category_analysis(df)
    monthly_totals = monthly_analysis(df)
    payment_totals = payment_analysis(df)
    budget = budget_analysis(df)

    # Generate charts
    create_visualizations(
        df,
        category_totals,
        monthly_totals,
        payment_totals
    )

    # Generate report
    generate_report(
        summary,
        category_totals,
        monthly_totals,
        payment_totals,
        budget
    )

    print("\n======================================")
    print("       PROJECT COMPLETED!")
    print("======================================")
    print("Check the images folder for charts.")
    print("Check the reports folder for the report.")


def main():

    parser = argparse.ArgumentParser(
        description="Personal Expense Tracker"
    )

    parser.add_argument(
        "--add",
        action="store_true",
        help="Add a new expense"
    )

    args = parser.parse_args()

    if args.add:
        print("\nADD A NEW EXPENSE")

        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        payment_method = input("Enter payment method: ")
        description = input("Enter description: ")

        add_expense(
            date,
            category,
            amount,
            payment_method,
            description
        )

    else:
        run_project()


if __name__ == "__main__":
    main()
