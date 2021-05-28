



def _uba_menu():
    PIN = 7600
    while True:
        print('1. Airtime-Self')
        print('2. Airtime-Others')
        print('3. Transfer-UBA')
        print('4. Transfer-Other Banks')
        print('5. Transfer-UBA Prepaid')
        print('6. Check-Balance')
        print('7. Pay Bills')
        print('8. Next')


        choice = int(input('> Enter your choice: '))

        if choice == 1:
            four_pin = int(input(">Please enter your PIN:\n"))

            if four_pin == PIN:
                amount = int(input("Please enter amount (50 - 10000):\n"))
                if type(amount) == int:
                    print("Your transaction is beign processed.\nNeed data? Dial *919*14# to buy\ndata now. #staysafe")
                elif type(amount) != int:
                    print("Invalid amount\n")
            elif four_pin != PIN:
                print('Invalid Pin. Please try again\n')
                return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                if return_menu == 1:
                    continue
                if return_menu == 2:
                    exit(0)

            return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
            if return_menu == 1:
                continue
            if return_menu == 2:
                exit(0)
        elif choice == 2:
            phone_no = int(input("Please enter destination phone line\nor the last four digits of the number.\n"))
            save_no = int(input("Would you like to save this\nbeneficiary?\n\n1.\tYes\n2.\tNo\n00.\tBack\n0.\tMain\n>"))

            if save_no == 1:
                print("Beneficiary saved sucessfully!", phone_no)
                four_pin = int(input(">Please enter your PIN:\n"))

                if four_pin == PIN:

                    amount = input("Please enter amount (50 - 10000):\n")
                    if type(amount) == int:
                        print("Your transaction is being processed.\nNeed data? Dial *919*14# to buy\ndata now. #staysafe")
                        exit(0)
                    elif type(amount) != int:
                        print("Invalid amount\n")
                elif four_pin != PIN:
                    print('Invalid Pin. Please try again\n')
                    return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                    if return_menu == 1:
                        continue

                    elif return_menu == 2:
                        exit(0)

            elif save_no == 2:
                four_pin = int(input(">Please enter your PIN:\n"))

                if four_pin == PIN:
                    amount = int(input("Please enter amount (50 - 10000):\n"))
                    if type(amount) == int:
                        print("Your transaction is being processed.\nNeed data? Dial *919*14# to buy\ndata now. #staysafe")
                    if type(amount) != int:
                        print("Invalid amount\n")

                elif four_pin != PIN:
                    print('Invalid Pin. Please try again\n')
                    return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                    if return_menu == 1:
                        continue
                    if return_menu == 2:
                        exit(0)
            elif save_no == 00:
                return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                if return_menu == 1:
                    continue
                elif return_menu == 2:
                    exit(0)
        elif choice == 3:

            account_no = int(input("Please enter the UBA account number\nor name of the beneficiary:\n\n00.\tBack\n0.\tMain\n\n>"))
            if account_no == 00:
                continue
            if account_no == 0:
                return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                if return_menu == 1:
                    continue

                elif return_menu == 2:
                    exit(0)

                print("Beneficiary saved sucessfully!", phone_no)
                four_pin = int(input(">Please enter your PIN:\n"))

                if four_pin == PIN:

                    amount = input("Please enter amount (50 - 10000):\n")
                    if type(amount) == int:
                        print(
                            "Your transaction is being processed.\nNeed data? Dial *919*14# to buy\ndata now. #staysafe")
                        exit(0)
                    elif type(amount) != int:
                        print("Invalid amount\n")
                elif four_pin != PIN:
                    print('Invalid Pin. Please try again\n')
                    return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                    if return_menu == 1:
                        continue

                    elif return_menu == 2:
                        exit(0)

            if account_no == account_no:

                bank = int(input("Please select bank:\n\n1. Bank 1\n2. Bank 2\n3. Bank 3\n4. Bank 4\n5. Bank 5\n>"))

                if bank in (1,2,3,4,5):
                    four_pin = int(input(">Please enter your PIN:\n"))
                    if four_pin == PIN:
                        amount = int(input("Send money to FIRST_NAME\nLAST_NAME.\nPlease enter amount (amount\n"
                                           "greater than NGN 20,000 will require\nSecure Pass):\n"))

                        if type(amount) == int:
                            print("Your transaction is being processed.\nNeed data? Dial *919*14# to buy\ndata now. #staysafe")

                        if type(amount) != int:
                            print("Invalid amount\n")

                    elif four_pin != PIN:
                        print('Invalid Pin. Please try again\n')
                        return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                        if return_menu == 1:
                            continue
                        if return_menu == 2:
                            exit(0)

            return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
            if return_menu == 1:
                continue
            if return_menu == 2:
                exit(0)
        elif choice == 4:
            print('Transfering to other banks\n')
            return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
            if return_menu == 1:
                continue
            if return_menu == 2:
                exit(0)
        elif choice == 5:
            print('Transfering to UBA prepaid\n')
            return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
            if return_menu == 1:
                continue
            if return_menu == 2:
                exit(0)
        elif choice == 6:
            print('Checking balance...\n')
            return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
            if return_menu == 1:
                continue
            if return_menu == 2:
                exit(0)
        elif choice == 7:
            print('Paying bills...\n')
            return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
            if return_menu == 1:
                continue
            if return_menu == 2:
                exit(0)
        elif choice == 8:
            print('1. Increase limit')
            print('2. Buy Data Self')
            print('3. Buy Data others')
            print('4. Cardless Withdrawal')
            print('5. Banking Services')
            print('6. Next')
            print('0. Back')

            option = int(input("Select option: "))
            if option == 1:
                print("Increasing limit...")
            elif option == 2:
                print("Buying Data Self...")
            elif option == 3:
                print("Buying Data others...")
            elif option == 4:
                print("Doing Cardless Withdrawal...")
            elif option == 5:
                print("Doing Banking Services")
            elif option == 6:
                print("Next")
            elif option == 0:
                return_menu = int(input("ENTER 1. TO BACK"))
                if return_menu == 1:
                    continue
                elif return_menu != 1:
                    print("Invalid input, please try again!")
            return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
            if return_menu == 1:
                continue
            if return_menu == 2:
                exit(0)

_uba_menu()