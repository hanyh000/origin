import time

class Account:
    def __init__(self, account_id, name, balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("입금 완료\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("출금액이 너무 큽니다.\n")
            return False
        else:
            self.balance -= amount
            print("출금 완료\n")
            return True

    def display(self):
        print(f"계좌ID: {self.account_id}")
        print(f"이름: {self.name}")
        print(f"잔액: {self.balance}원\n")

class ATM:
    def __init__(self):
        self.accounts = {}  # 계좌ID를 키로 갖는 딕셔너리로 계좌 저장

    def create_account(self):
        print("[계좌개설]\n")
        try:
            account_id = input("계좌ID (숫자로 입력): ")
            if account_id in self.accounts:
                print("이미 존재하는 계좌 ID입니다.\n")
                return
            name = input("이름: ")
            balance = int(input("입금액: "))
            self.accounts[account_id] = Account(account_id, name, balance)
            print("계좌가 성공적으로 개설되었습니다.\n")
        except ValueError:
            print("잘못된 입력입니다. 입금액은 숫자로 입력하세요.\n")

    def deposit(self):
        print("[입  금]\n")
        try:
            account_id = input("계좌ID (숫자로 입력): ")
            if account_id not in self.accounts:
                print("유효하지 않은 ID입니다.\n")
                return
            amount = int(input("입금액: "))
            self.accounts[account_id].deposit(amount)
        except ValueError:
            print("입금액은 숫자여야 합니다.\n")

    def withdraw(self):
        print("[출  금]\n")
        try:
            account_id = input("계좌ID (숫자로 입력): ")
            if account_id not in self.accounts:
                print("유효하지 않은 ID입니다.\n")
                return
            amount = int(input("출금액: "))
            self.accounts[account_id].withdraw(amount)
        except ValueError:
            print("출금액은 숫자여야 합니다.\n")

    def display_all_accounts(self):
        print("[전체 계좌 출력]\n")
        if not self.accounts:
            print("등록된 계좌가 없습니다.\n")
            return
        for acc in self.accounts.values():
            acc.display()

    def run(self):
        while True:
            print("-----Menu-----\n")
            print("1. 계좌개설")
            print("2. 입금")
            print("3. 출금")
            print("4. 계좌번호 전체 출력")
            print("5. 프로그램 종료")
            try:
                choice = int(input("선택(1~5): "))
                if choice == 1:
                    self.create_account()
                elif choice == 2:
                    self.deposit()
                elif choice == 3:
                    self.withdraw()
                elif choice == 4:
                    self.display_all_accounts()
                elif choice == 5:
                    print("프로그램을 종료합니다.")
                    break
                else:
                    print("1~5 사이의 숫자를 입력하세요.\n")
            except ValueError:
                print("정수를 입력하지 않았습니다.\n")
            time.sleep(2)

# 실행
atm = ATM()
atm.run()
