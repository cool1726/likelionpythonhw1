from UserDB.User import *

userDB = []

class Account(User):
    def __init__(self):
        pass

    def newAcc(self):
        print("     <Create account>")
        accountNum = input(" * Enter the account number : ")
        for user in userDB:
            if accountNum == user.accountNum:
                print("     SAME ACCOUNT ALREADY EXISTS")
                return 0
        self.accountNum = accountNum
        self.name = input(" * Enter your name : ")
        self.accountBal = int(input(" * Deposit amount : "))
        userDB.append(acc)
        print(" * Create Account Complete")


    def deposit(self):
        print("     <Deposit>")
        if len(userDB) == 0:
            print("     NO ACCOUNT EXISTS")
            return 0
        account_temp = input(" * Enter the account number : ")
        for user in userDB:
            if account_temp == user.accountNum:
                print(" * Account NAME : ", user.name)
                print(" * Account BALANCE : ", user.accountBal)
                deposit_string = input(" * Please enter the amount you deposit : ")
                isDecimal = deposit_string.isdecimal()
                if (not isDecimal): # 입력금액이 숫자가 아닐때
                    print("     INVAILD INPUT")
                elif int(deposit_string) < 0 :  # 입력금액이 음수일때
                    print("     INVAILD INPUT")
                elif int(deposit_string) <= user.accountBal:    # 입력금액 < 잔고 : 정상작동
                    user.accountBal += int(deposit_string)
                    print(" * Account Balance : ", user.accountBal, "won")
                    print(" * Deposit Complete")
                else:
                    print("     NOT ENOUGH BALANCE")
                return 0
            else:
                if (user == userDB[-1]):
                    print("     INVALID ACCOUNT NUMBER")
                    break


    def withdraw(self):
        print("     <Withdraw>")
        if len(userDB) == 0:
            print("     NO ACCOUNT EXISTS")
            return 0
        account_temp = input(" * Enter the account number : ")
        for user in userDB:
            if account_temp == user.accountNum:
                print(" * Account NAME : ", user.name)
                print(" * Account BALANCE : ", user.accountBal)
                withdraw_string = input(" * Please enter the amount you withdraw : ")
                isDecimal = withdraw_string.isdecimal()
                if (not isDecimal):
                    print("     INVAILD INPUT")
                elif int(withdraw_string) < 0 :
                    print("     INVAILD INPUT")
                elif int(withdraw_string) <= user.accountBal:
                    user.accountBal -= int(withdraw_string)
                    print(" * Account Balance : ", user.accountBal, "won")
                    print(" * Withdraw Complete")
                else:
                    print("     NOT ENOUGH BALANCE")
                return 0
            else:
                if (user == userDB[-1]):
                    print("     INVALID ACCOUNT NUMBER")
                    break


    def readAcc(self):
        if len(userDB) == 0:
            print("     NO ACCOUNT EXISTS")
        else:
            print("     <View all accounts>")
            for user in userDB:
                print("Account Number: ", user.accountNum, "/ UserName: ", user.name, "/ Balance: ", user.accountBal, "won")


if __name__ == "__main__":
    while True:
        print()
        print("_____<Select the Menu>_____")
        print("| 1. Create account       |")
        print("| 2. Deposit              |")
        print("| 3. Withdraw             |")
        print("| 4. Checking account     |")
        print("| 5. Completion           |")
        print("---------------------------")
        menu_num = int(input("Press the menu num : "))

        acc = Account()

        # 1. 계좌개설
        if menu_num == 1:
            acc.newAcc()

        # 2. 입금하기
        elif menu_num == 2:
            acc.deposit()

        # 3. 출금하기
        elif menu_num == 3:
            acc.withdraw()

        # 4. 계좌조회
        elif menu_num == 4:
            acc.readAcc()

        # 5. 프로그램 종료
        elif menu_num == 5:
            print("     <End of program>")
            break

        else:
            print("     <INPUT WRONG NUMBER>")
