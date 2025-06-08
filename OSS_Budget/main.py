import datetime
from budget import Budget
from budget goal import goal
from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 목표 추가")
        print("5. 목표 목록 보기")
        print("6. 저축 추가")
        print("7. 저축 목록 보기")
        print("8. 총 저축 보기")
        print("9. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            content = input("아자아자 아껴쓰자! 나의 목표 : ")
            budget.add_goal(content)

        elif choice == "5":  
            budget.list_goals()

        elif choice == "6": 
            category = input("카테고리 (예: 생활비, 투자 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_saving(category, description, amount)
            
        elif choice == "7": 
            budget.list_saving()
            
        elif choice == "8":  
            budget.total_saving()

        elif choice == "9":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
