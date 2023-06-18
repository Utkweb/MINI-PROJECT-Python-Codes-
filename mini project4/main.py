from money import Money

def get_integer(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError(f"Value must be greater than or equal to {min_val}")
            if max_val is not None and value > max_val:
                raise ValueError(f"Value must be less than or equal to {max_val}")
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    # Create a Money object to keep track of the balance in the account
    balance = Money()

    # current =0.0

    while True:
        # Display menu options     
        print("\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. See current balance")
        print("4. Exit")

        choice = get_integer("Enter your choice (1-4):", min_val=1, max_val=4)


        if choice == 1:
            # Deposit
            print("Deposit")
            dollars = get_integer("Enter dollars (0-1000): ", min_val=0, max_val=1000)
            cents = get_integer("Enter cents (0-99): ", min_val=0, max_val=99)
            deposit = Money(dollars, cents)

            
            balance += deposit
            print("Transaction completed. ")
        elif choice == 2:
            # Withdraw
            print("Withdraw")
            dollars = get_integer("Enter dollars (0-1000): ", min_val=0, max_val=1000)
            cents = get_integer("Enter cents (0-99): ", min_val=0, max_val=99)
            withdrawal = Money(dollars, cents)

            # if (balance >= withdrawal):

            balance -= withdrawal
            print("Transaction completed. ")

            # else:
            #     print("Error: Not enough funds in the account.")
        elif choice == 3:
            # See current balance
            print(f"Your current balance is: {balance}")
        else:
            # Exit
            print("Good-bye!")
            break
        # else:
        #     print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

