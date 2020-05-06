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
                deposit_temp = int(input(" * Please enter the amount you deposit : "))
                if deposit_temp < 0:
                    print("     INVAILD INPUT")
                else:
                    user.accountBal += deposit_temp
                    print(" * Account Balance : ", user.accountBal, "원")
                    print(" * Deposit Complete")
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
                withdraw_temp = int(input(" * Please enter the amount you withdraw : "))
                if withdraw_temp < 0:
                    print("     INVAILD INPUT")
                elif withdraw_temp <= user.accountBal:
                    user.accountBal -= withdraw_temp
                    print(" * Account Balance : ", user.accountBal, "원")
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
                print("Account Number: ", user.accountNum, "/ UserName: ", user.name, "/ Balance: ", user.accountBal, "원")


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
