import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

   def category_summary(self):
    """카테고리별 지출 합계 계산"""
    summary = {}
    for expense in self.expenses:
        if expense.category in summary:
            summary[expense.category] += expense.amount
        else:
            summary[expense.category] = expense.amount
    
    print("\n[카테고리별 지출 현황]")
    for category, total in summary.items():
        print(f"{category}: {total}원")
    print(f"\n총 지출: {sum(summary.values())}원\n")
