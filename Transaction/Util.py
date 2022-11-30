import random
import string


def random_string(length: int) -> str:
    """
    Fungsi ini untuk menghasilkan random huruf untuk mengidentifikasikan id daripada setiap produk/items yang ditambahkan oleh pengguna.
    """
    result_id = ''.join(random.choice(string.ascii_letters)
                        for i in range(length))
    return result_id
