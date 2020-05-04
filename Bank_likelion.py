while True:
    print("_____<Select the Menu>_____")
    print("| 1. Creat account        |")
    print("| 2. Deposit              |")
    print("| 3. Withdraw             |")
    print("| 4. Checking account     |")
    print("| 5. Completion           |")
    print("---------------------------")
    menu_num = int(input("Press the buton : "))
    #print(menu_num) 제대로 들어갔는지 확인
    #계좌개설
    if menu_num == 1:
        print("     <Creat account>")
        account = [0,' ',0]
        account[0] = int(input(" * Enter the account number : "))
        account[1] = str(input(" * Enter your account name : "))
        account[2] = int(input(" * Deposit : "))
        print(" * Creat Account Complete")

    #입금하기
    elif menu_num == 2:
        print("     <Deposit>")
        account_temp = int(input(" * Enter your account number : "))
        if account_temp == account[0]:
            print(" * Account NAME : ", account[1])
            print(" * Account BALANCE : ", account[2])
            deposit_temp = int(input(" * Please enter the amount you deposit : "))
            account[2] = account[2] + deposit_temp
            print(" * Account Balance :",account[2])
            print(" * Deposit Complete")
        else:
            print("     INVALID ACCOUNT NUMBER")
            continue

    #출금하기
    elif menu_num == 3:
        print("     <Withdraw>")
        account_temp = int(input(" * Enter your account number : "))
        if account_temp == account[0]:
            print(" * Account NAME : ",account[1])
            print(" * Account BALANCE : ",account[2])
            withdraw_temp = int(input(" * Please enter the amount you withdraw : "))
            if account[2] >= withdraw_temp:
                account[2] = account[2] - withdraw_temp
                print(" * Account Balance : ",account[2])
                print(" * Withdraw Complete")
            else:
                print("     NOT ENOUGH BALANCE")
                continue
        else:
            print("     INVALID ACCOUNT NUMBER")
            continue
    #계좌조회
    elif menu_num == 4:
        print("     <Checking account>")
        for i in account:
            print(i)

    elif menu_num == 5:
        print("     <End of program>")

        break
    else:
        print("     <INPUT WRONG NUMBER>")