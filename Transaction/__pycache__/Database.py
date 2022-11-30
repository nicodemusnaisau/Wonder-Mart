from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "id_product": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "item": 255*" ",
    "QTY": 255*" ",
    "price": "yyyy",
    "total_harga": "y.yyy"
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database berhasil dibuat!")
    except:
        print("Database tidak tersedia.")
        Operasi.create_first_data()
