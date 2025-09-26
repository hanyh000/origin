import time
class Atm:

   def menu(self, account, income, outcome, all, exit ): 
      self.account = account
      self.income =income
      self.outcome = outcome
      self.all = all
      self.exit = exit

a1=0
a2 = 0
n=0
i=0
s=0
while True:
    try:
        print("-----Menu-----\n")
        print("1. 계좌개설\n")
        print("2. 입금\n")
        print("3. 출금\n")
        print("4. 계좌번호 전체 출력\n")
        print("5. 프로그램 종료\n")
        number = input("선택(1~5까지의 숫자만 입력) : ")
        number = int(number)
        if number == 1:
            print("[계좌개설]\n")
            a1 = input("계좌ID:(숫자로 입력) ")
            n = input("이름: ")
            i = int(input("입금액: "))
            s = i
        if number == 2:
            print("[입  금]\n")
            a2 = input("계좌ID:(숫자로 입력) ")
            i = int(input("입금액: "))
            if a2 != a1 :
                print("유효하지 않은 ID입니다.\n")
            else :
                s +=i
                print("입금완료\n")
        if number == 3:
            print("[출  금]\n")
            a2 = input("계좌ID:(숫자로 입력) ")
            i = int(input("출금액: "))
            if a2 != a1 :
                print("유효하지 않은 ID입니다.\n")
            else :
                s -=i
                if s<0:
                    print("출금액이 너무 큽니다.")
                    s+=i
                else:
                    print("출금완료\n")
        if number == 4:
            print("계좌ID:{}\n".format(a1))
            print("이름: {}\n".format(n))
            print("잔액: {}\n".format(s))
        if number == 5:
            break
    except:
        print("정수를 입력하지 않았습니다.")
    time.sleep(5)