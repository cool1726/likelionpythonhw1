users = []

class User:
    name = '이름'
    accountNum = '계좌번호'
    accountBal = 0

class Account(User):
    def __init__(self):
        print("     <Create account>")
        accountNum = input(" * Enter the account number : ")
        for user in users:
            if accountNum == user.accountNum:
                print(" ** Same Account already exists")
                continue
        self.accountNum = accountNum
        self.name = input(" * Enter your name : ")
        self.accountBal = int(input(" * Deposit amount : "))
        print(" * Create Account Complete")

    def deposit(self, amount):
        self.accountBal += amount

    def withdraw(self, amount):
        self.accountBal -= amount

    def readAcc(self):
        print("Account Number: ", user.accountNum, "/ UserName: ", user.name, "/ Balance: ", user.accountBal, "원")



if __name__ == "__main__" :
    while True :
        print("---------------------------")
        print("_____<Select the Menu>_____")
        print("| 1. Create account       |")
        print("| 2. Deposit              |")
        print("| 3. Withdraw             |")
        print("| 4. Checking account     |")
        print("| 5. Completion           |")
        print("---------------------------")
        menu_num = int(input("Press the menu num : "))

        # 1. 계좌개설
        if menu_num == 1:
            createAcc = Account()
            users.append(createAcc)

        # 2. 입금하기
        elif menu_num == 2:
            print("     <Deposit>")
            account_temp = input(" * Enter the account number : ")
            for user in users:
                if account_temp == user.accountNum:
                    print(" * Account NAME : ", user.name)
                    print(" * Account BALANCE : ", user.accountBal)
                    deposit_temp = int(input(" * Please enter the amount you deposit : "))
                    user.deposit(deposit_temp)
                    print(" * Account Balance : ", user.accountBal, "원")
                    print(" * Deposit Complete")
                    break
                else:
                    if (user == users[-1]):
                        print("     INVALID ACCOUNT NUMBER")
                        break


        # 3. 출금하기
        elif menu_num == 3:
            print("     <Withdraw>")
            account_temp = input(" * Enter the account number : ")
            for user in users:
                if account_temp == user.accountNum:
                    print(" * Account NAME : ", user.name)
                    print(" * Account BALANCE : ", user.accountBal)
                    withdraw_temp = int(input(" * Please enter the amount you withdraw : "))
                    if withdraw_temp <= user.accountBal:
                        user.withdraw(withdraw_temp)
                        print(" * Account Balance : ", user.accountBal, "원")
                        print(" * Deposit Complete")
                    else:
                        print("     NOT ENOUGH BALANCE")
                        break
                else:
                    if (user == users[-1]):
                        print("     INVALID ACCOUNT NUMBER")
                        break

        # 4. 계좌조회
        elif menu_num == 4:
            print("     <View all accounts>")
            for user in users:
                user.readAcc()

        # 5. 프로그램 종료
        elif menu_num == 5:
            print("     <End of program>")
            break

        else:
            print("     <INPUT WRONG NUMBER>")
