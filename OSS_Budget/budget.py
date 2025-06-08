import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
	self.goals=[]

    def add_goal(self, content):
        today = datetime.date.today().isoformat()
        goal = Goal(today, content)
        self.goals.append(goal)
        print("목표가 추가되었습니다.\n")

    def list_goals(self):
        if not self.goals:
            print("목표가 설정되지 않았습니다...\n")
            return
        print("\n[나의 목표 목록]")
        for idx, goal in enumerate(self.goals, 1):
            print(f"{idx}. {goal}")
        print()

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


