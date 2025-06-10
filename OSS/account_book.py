import csv
import os

FILENAME = "account_book.csv"

def load_data():
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)
    return data

def save_data(data):
    with open(FILENAME, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def add_entry(data):
    date = input("날짜 입력(YYYY-MM-DD): ")
    amount = input("금액 입력: ")
    description = input("항목명 입력: ")
    kind = input("수입/지출 선택(수입:1, 지출:2): ")
    kind_str = "수입" if kind == "1" else "지출"
    data.append([date, amount, description, kind_str])
    print("내역이 추가되었습니다.")

def view_entries(data):
    print("=== 내역 목록 ===")
    for entry in data:
        print(entry)

def monthly_summary(data):
    month = input("확인할 월 입력 (YYYY-MM): ")
    income, expense = 0, 0
    for entry in data:
        if entry[0].startswith(month):
            if entry[3] == "수입":
                income += int(entry[1])
            else:
                expense += int(entry[1])
    print(f"{month} 수입: {income}원, 지출: {expense}원, 잔액: {income-expense}원")

def main():
    data = load_data()
    while True:
        print("\n1. 내역 추가\n2. 내역 조회\n3. 월별 잔액 확인\n4. 저장 및 종료")
        choice = input("메뉴 선택: ")
        if choice == "1":
            add_entry(data)
        elif choice == "2":
            view_entries(data)
        elif choice == "3":
            monthly_summary(data)
        elif choice == "4":
            save_data(data)
            print("저장 후 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
