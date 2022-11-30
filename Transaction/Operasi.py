from time import time
from . import Database
from . import View
from .Util import random_string
from colored import stylize
from colored import fg, bg, attr
import time
import os
import babel.numbers
import colored


def create_first_data():
    """
    Fungsi ini bertujuan untuk dapat melakukan create data saat pertama kali user menggunakan program. Ketika program berjalan namun tidak terdapat file data.txt
    maka User akan diarahkan untuk menambahkan Item pesanan. Setelah ditambahkan maka akan dibuat file data.txt yang memuat informasi pesanan pengguna.
    """
    item = input("item: ")
    QTY = int(input("Quantity\t: "))
    price = float(input("Price\t: "))
    total_harga = float(price)*(int(QTY))
    data = Database.TEMPLATE.copy()
    data["id_product"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["item"] = item + Database.TEMPLATE["item"][len(item):]
    data["QTY"] = int(QTY)
    data["price"] = int(price)
    data["total_harga"] = total_harga
    data_str = f'{data["id_product"]},{data["date_add"]},{data["QTY"]},{data["item"]},{data["price"]},{data["total_harga"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("<create_first_data> Data tidak dapat ditambahkan")


def create(price, item, QTY):
    """
    Fungsi ini akan menerima 3 parameter di antaranya item, quantity, dan price yang diinput berdasarkan modul View.py.
    Data yang diimput akan diterima oleh database dengan menerapkan fungsi Append dan encoding utf-8
    """
    data = Database.TEMPLATE.copy()
    data["id_product"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["item"] = item + Database.TEMPLATE["item"][len(item):]
    data["QTY"] = int(QTY)
    data["price"] = int(price)
    data["total_harga"] = float(price*QTY)

    data_str = f'{data["id_product"]},{data["date_add"]},{data["QTY"]},{data["item"]},{data["price"]},{data["total_harga"]}\n'

    try:
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("<create> Data tidak dapat ditambahkan")


def update(no_item, id_product, date_add, price, item, QTY):
    """
    Fungsi ini menerima data dari View.py yang telah dilakukan operasi pada Pengguna dengan menerima data di antaranya adalah
    no_item yang merupakan index daripada item belanja, id_product yang merupakan random_id, date_add merupakan tanggal data tersebut ditambahkan, price, item, dan quantity
    merupakan input yang akan diperbaharui
    """
    data = Database.TEMPLATE.copy()
    data["id_product"] = id_product
    data["date_add"] = date_add
    data["item"] = item + Database.TEMPLATE["item"][len(item):]
    data["QTY"] = int(QTY)
    data["price"] = int(price)
    data["total_harga"] = float(int(price)*int(QTY))
    data_str = f'{data["id_product"]},{data["date_add"]},{data["QTY"]},{data["item"]},{data["price"]},{data["total_harga"]}\n'
    panjang_data = len(data_str)
    # handling error
    try:
        with open(Database.DB_NAME, 'r+', encoding="utf-8") as file:
            file.seek(panjang_data*(no_item-1))
            file.write(data_str)
    except:
        print("<update> Tidak dapat update Database")


def read(**kwargs):
    """
    Fungsi ini untuk membaca keseluruhan data pada data.txt
    """
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            item = len(content)
            if "index" in kwargs:
                index_item = kwargs["index"]-1
                if index_item < 0 or index_item > item:
                    return False
                else:
                    return content[index_item]
            else:
                return content
    except:
        return False


def total_price():
    """
    Fungsi ini untuk melakukan kalkulasi terhadap total keseluruhan belanja pada keranjang belanajaan dengan ketentuan discount yang telah ditentukan.
    """

    data_file = read()
    purchase_price = 0
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        total_harga = data_break[5]
        purchase_price += float(total_harga)
    x = ""  # hmm i just want empty space, not empty moneey
    purchase_price_total = babel.numbers.format_currency(
        purchase_price, 'Rp', locale="ID")
    print(f"Price {x:62}   {purchase_price_total:10}")

    if purchase_price < 200_000:
        print(f"Promo Discount  {x:62}  - ")
        print("_"*100)
        print(
            f"Total Payment{x:55}   {fg(208)}{purchase_price_total:10}{attr(0)}")

    if purchase_price >= 200_000 and purchase_price < 300_000:
        discount_calcaulate = babel.numbers.format_currency(
            (purchase_price*0.05), 'Rp-', locale="ID")
        print(
            f"Promo Discount 5% {x:50}   {fg(78)}{discount_calcaulate:10}{attr(0)}")
        print("_"*100)
        payment_after_discount = babel.numbers.format_currency(
            purchase_price - (purchase_price*0.05), 'Rp', locale="ID")
        print(
            f"Total Payment{x:55}   {fg(208)}{payment_after_discount:10}{attr(0)}")

    elif purchase_price >= 300_000 and purchase_price < 500_000:
        discount_calcaulate = babel.numbers.format_currency(
            (purchase_price*0.08), 'Rp-', locale="ID")
        print(
            f"Promo Discount 8% {x:50}   {fg(78)}{discount_calcaulate:10}{attr(0)}")
        print("_"*100)
        payment_after_discount = babel.numbers.format_currency(
            purchase_price - (purchase_price*0.08), 'Rp', locale="ID")
        print(
            f"Total Payment{x:55}   {fg(208)}{payment_after_discount:10}{attr(0)}")

    elif purchase_price >= 500_000:
        discount_calcaulate = babel.numbers.format_currency(
            (purchase_price*0.10), 'Rp-', locale="ID")
        print(
            f"Promo Discount 10% {x:50}   {fg(78)}{discount_calcaulate:10}{attr(0)}")
        print("_"*100)
        payment_after_discount = babel.numbers.format_currency(
            purchase_price - (purchase_price*0.10), 'Rp', locale="ID")
        print(
            f"Total Payment{x:55}   {fg(208)}{payment_after_discount:10}{attr(0)}")


def delete(no_item):
    """
    Fungsi ini untuk dapat melakukan delete data pada data.txt, dengan melakukan pengecekan terhadap data yang akan dipilih serta tidak mengikutsertakan data tersebut ke dalam file baru yang disimpan di dalam transaction_temp.txt. kemudian akan menggunakan os.replace untuk mengganti transaction_temp ke data.txt yang baru sehingga data yang dipilih tersebut sudah terhapus
    """
    try:
        with open(Database.DB_NAME, 'r') as file:
            counter = 0
            while (True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_item - 1:
                    pass
                else:
                    with open("transaction_temp.txt", 'a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Failed to delete item")
    try:
        os.replace("transaction_temp.txt", Database.DB_NAME)
        print("items successfully deleted")
    except (FileNotFoundError):  # not effective aowkaowk, i dont know why cannot find transaction_temp.txt if only 1 data added
        reset()
        print("items successfully deleted")


def reset():
    """
    Fungsi ini untuk melakukan penghapusan keseluruhan data pada file data.txt
    """
    try:
        with open(Database.DB_NAME, 'r') as file:
            with open("transaction_temp.txt", 'a', encoding="utf-8") as temp_file:
                temp_file.write()
    except:
        pass

    os.replace("transaction_temp.txt", Database.DB_NAME)
