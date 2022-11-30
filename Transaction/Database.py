from . import Operasi

"""
Format untuk mengatur template dari data yang diterima, mendefinisikan setiap variabel dengan ketentuanya masing-masing
"""

DB_NAME = "data.txt"
TEMPLATE = {
    "id_product": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "item": 255*" ",
    "QTY": 255*" ",
    "price": "xxxx",
    "total_harga": "xxxx"
}


def init_console():
    """
    Fungsi ini untuk melakukan pengecekan terhadap database atau file data.txt tersedia atau tidak, ketika program dijalankan tidak ditemukan, maka pengguna akan diminta melakukan input data item terlebih dahulu
    """
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
