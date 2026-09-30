"""Modul untuk demonstrasi Pylint quality gate."""


def kali(a, b):
    """Mengalikan dua angka."""
    return a * b


def main():
    """Fungsi utama program."""
    hasil = kali(5, 10)
    print(hasil)


if __name__ == "__main__":
    main()
