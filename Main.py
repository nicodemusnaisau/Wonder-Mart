import Transaction as Transaction
from colored import fg, bg, attr
from colored import stylize


if __name__ == "__main__":

    Transaction.clean_console()
    Transaction.init_console()

    while (True):

        Transaction.clean_console()

        print("Welcome to WONDER Mart")
        print("----------------------------")
        print(f"1. My Cart")
        print(f"2. Add Item")
        print(f"3. Update Item")
        print(f"4. Delete Item")
        print(f"5. Payment Details")
        print(f"6. Reset Transaction")
        print(f"7. Exit\n")

        user_option = input("Menu: ")

        match user_option:
            case "1": Transaction.read_console()
            case "2": Transaction.create_console()
            case "3": Transaction.update_console()
            case "4": Transaction.delete_console()
            case "5": Transaction.payment_summary()
            case "6": Transaction.reset_console()
            case "7": Transaction.exit()

        is_done = input("Back to main menu (y/n)? ")

        match is_done:
            case "y":
                pass
            case "Y":
                pass
            case "n":
                is_done_confirm = input("Are you sure? :")
                if is_done_confirm == 'y' or is_done_confirm == 'Y':
                    Transaction.exit()
                    break
                pass
            case "N":
                is_done_confirm = input("Are you sure? :")
                if is_done_confirm == 'y' or is_done_confirm == 'Y':
                    Transaction.exit()
                    break
                pass
