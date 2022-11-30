from . import Operasi
from . import Database
from colored import stylize
from colored import fg, bg, attr
import sys
import os
import babel.numbers
import colored


def delete_console():
    """
    Pada fungsi ini akan melakukan interaksi dengan pengguna melalui console, dengan data tersebut akan dilakukan operasi delete yang terdapat pada modul Operasi.py
    """
    read_console()

    while (True):
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            item = len(content)
            if item == 0:
                print("Hello, is something wrong?")
                print(
                    "You seem to haven't ordered any items yet, just check our menu, it's not rocket science")
                break

        print("Remove Item")
        no_item = int(input("Number of item: "))
        data_item = Operasi.read(index=no_item)

        if data_item:
            data_break = data_item.split(',')
            QTY = data_break[2]
            item = data_break[3]
            price = data_break[4]

            # confirm data before delete
            print("\n"+"="*100)
            print("Want to remove item?")
            print(f"1. Item Name\t: {item:.40}")
            print(f"2. Quantity\t: {QTY:.40}")
            print(f"3. Price\t: {price:4}")
            is_done = input(
                f"{fg(1)}Are you sure want to remove this item from your cart? (y/n)? {attr(0)}")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_item)
                
                break
        else:
            print("invalid input")


def reset_console():
    """
    Pada fungsi ini akan melakukan interaksi dengan pengguna melalui console, dengan data tersebut akan dilakukan operasi reset yang terdapat pada modul Operasi.py
    """
    read_console()
    is_done = input(
        f"{fg(1)}Are you sure want to delete all items from your cart? (y/n)? {attr(0)}")
    if is_done == "y" or is_done == "Y":
        Operasi.reset()
        print("all items successfully deleted")
    else:
        print("fail to delete")


def update_console():
    """
    Pada fungsi ini akan melakukan interaksi dengan pengguna melalui console, dengan data tersebut akan dilakukan operasi update yang terdapat pada modul Operasi.py
    """
    read_console()
    with open(Database.DB_NAME, 'r') as file:
        content = file.readlines()
        item = len(content)
        if item == 0:
            print("Hello, is something wrong?")
            print(
                "You seem to haven't ordered any items yet, just check our menu, it's not rocket science :D")
        else:
            while (True):
                print("Want to change your item(s)?")
                print("Please select index number")
                while (True):
                    try:
                        no_item = int(input("item number: "))
                        if int(no_item):
                            break
                    except (ValueError):
                        print("oops, make sure number :), please enter it again")

                data_item = Operasi.read(index=no_item)
                if data_item:
                    break
                else:
                    print("oops... we could'nt find the index. please fill it again\n")

    if item != 0:
        data_break = data_item.split(',')
        id_product = data_break[0]
        date_add = data_break[1]
        QTY = data_break[2]
        item = data_break[3]
        price = data_break[4]
        while (True):
            # items shows
            print("\n"+"="*100)
            print("Update item")
            print(f"1. item\t: {item:.40}")
            print(f"2. QTY\t: {QTY:.40}")
            print(f"3. Price: {price:4}")

            # option in detail items update
            user_option = input("Choose data [1,2,3]: ")
            print("\n"+"="*100)
            match user_option:
                case "1": item = input("item\t: ")
                case "2":
                    while (True):
                        try:
                            QTY = input("QTY\t: ")
                            if int(QTY):
                                break
                        except (ValueError):
                            print(
                                "oops, make sure number :), please enter it again")
                case "3":
                    while (True):
                        try:
                            price = int(input("Price\t: "))
                            if int(price) or float(price):
                                break
                        except (ValueError):
                            print(
                                "oops... price be number, please enter it again")
                case _: print("oops... we couldn't find the index")

            print("Item Update\n")
            print(f"1. item\t: {item:.40}")
            print(f"2. QTY\t: {QTY:.40}")
            print(f"3. Price: {price:4}")
            is_done = input("are you sure?(y/n) ")
            if is_done == "y" or is_done == "Y":
                break
            else:
                print("oops, failed to update items, please try again\n")
                return False

        Operasi.update(no_item, id_product, date_add, price, item, QTY)
        print(f"{fg(2)}yeay, successfully updated{attr(0)}")


def create_console():
    """
    Pada fungsi ini akan melakukan interaksi dengan pengguna melalui console, dengan data tersebut akan dilakukan operasi menambahkan items yang terdapat pada modul Operasi.py
    """
    print("\n\n"+"="*100)
    print("Add to Cart\n")
    item = input("item\t: ")
    while (True):
        try:
            QTY = int(input("QTY\t: "))
            if int(QTY):
                break
        except (ValueError):
            print("oops, make sure number :), please enter it again")

    while (True):
        try:
            price = int(input("Price\t: "))
            if (int(price)) or (float(price)):
                break
        except (ValueError):
            print("oops, make sure number :), please enter it again")

    Operasi.create(price, item, QTY)
    print(f"\n {fg(2)}yeay, Added Item to chart{attr(0)}")
    read_console()


def read_console():
    """
    Melakukan pemanggilan data yang terdapat pada fungsi Operasi
    """
    data_file = Operasi.read()
    index = "No"
    item = "item"
    QTY = "QTY"
    price = "Price"
    total_harga = "Sub Total"
    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {item:23} | {QTY:4} | {price:10} | {total_harga:10}")
    print("-"*100)

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")

        QTY = data_break[2]
        item = data_break[3]
        price = data_break[4]
        sum_price = data_break[5]
        currency_harga = babel.numbers.format_currency(
            sum_price, 'Rp', locale="ID")

        print(
            f"{index+1:4} | {item:.23} | {QTY:4} | {price:10} | {currency_harga:10}")

    # Footer
    print("="*100)


def payment_summary():
    """
    Pada fungsi ini akan melakukan interaksi dengan pengguna melalui console, dengan data tersebut akan dilakukan operasi kalkulasi price yang terdapat pada modul Operasi.py
    """
    read_console()
    with open(Database.DB_NAME, 'r') as file:
        content = file.readlines()
        item = len(content)
        if item == 0:
            print("Hello, is something wrong?")
            print(
                "You seem to haven't ordered any items yet, just check our menu, it's not rocket science")

    print("Payment Details")
    print("-"*100)
    Operasi.total_price()
    print("="*100+"\n")


def exit():
    """
    Pada fungsi ini akan melakukan interaksi dengan pengguna melalui console, dengan data tersebut akan dilakukan exit program.
    """
    Operasi.reset()
    sys.exit("Thanks for using WonderMart")


def clean_console():
    """
    Pada fungsi ini akan melakukan interaksi dengan pengguna melalui console, melakukan clear console dengan menyesuaikan sistem operasi yang dipakai pengguna.
    """
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
