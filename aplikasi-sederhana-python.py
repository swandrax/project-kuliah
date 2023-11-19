import hashlib
import os
import json
import getpass

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk membuat hash MD5 dari kata sandi
def generate_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

# Fungsi untuk menyimpan data tamu ke dalam file JSON
def save_guest_data(guest_data):
    with open('guests.json', 'w') as file:
        json.dump(guest_data, file)

# Fungsi untuk memuat data tamu dari file JSON
def load_guest_data():
    if os.path.exists('guests.json'):
        with open('guests.json', 'r') as file:
            return json.load(file)
    else:
        return {}

# Fungsi untuk mendaftarkan tamu baru
def register():
    print("=== Pendaftaran Tamu ===")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    hashed_password = generate_md5(password)

    guest_data = load_guest_data()
    if username in guest_data:
        print("Username sudah digunakan. Silakan pilih username lain.")
    else:
        guest_data[username] = {'password': hashed_password}
        save_guest_data(guest_data)
        print("Pendaftaran berhasil!")

# Fungsi untuk melakukan login tamu
def login():
    print("=== Login Tamu ===")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    hashed_password = generate_md5(password)

    guest_data = load_guest_data()
    if username in guest_data and guest_data[username]['password'] == hashed_password:
        print("Login berhasil!")
        input("Tekan Enter untuk melanjutkan...")
        return True
    else:
        print("Login gagal. Periksa kembali username dan password.")
        input("Tekan Enter untuk melanjutkan...")
        return False

# Fungsi untuk menampilkan menu utama
def main_menu():
    while True:
        clear_screen()
        print("=== Aplikasi Peminjaman Buku ===")
        print("1. Login Tamu")
        print("2. Pendaftaran Tamu")
        print("3. Keluar")
        choice = input("Pilihan Anda: ")

        if choice == '1':
            if login():
                book_menu()
        elif choice == '2':
            register()
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menampilkan menu peminjaman buku
def book_menu():

    # Contoh sederhana:
    print("\n=== Menu Peminjaman Buku ===")
    print("1. Lihat Daftar Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Keluar")

    choice = input("Pilihan Anda: ")

    if choice == '1':
        show_book_list()
    elif choice == '2':
        borrow_book()
    elif choice == '3':
        return_book()
    elif choice == '4':
        print("Terima kasih! Sampai jumpa.")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        book_menu()

# Fungsi untuk menampilkan daftar buku
def show_book_list():
    # Di sini Anda dapat menampilkan daftar buku dari file JSON atau database.
    # Contoh sederhana:
    print("\n=== Daftar Buku ===")
    book_list = ["Buku 1", "Buku 2", "Buku 3"]
    for i, book in enumerate(book_list, start=1):
        print(f"{i}. {book}")

    input("Tekan Enter untuk melanjutkan...")
    book_menu()

# Fungsi untuk meminjam buku
def borrow_book():
    # Di sini Anda dapat menambahkan logika untuk meminjam buku dan
    # menyimpan data peminjaman ke dalam file JSON atau database.
    # Contoh sederhana:
    book_id = input("Masukkan ID buku yang ingin dipinjam: ")
    return_date = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ")

    print("\nBuku berhasil dipinjam!")
    print(f"Harap mengembalikan buku sebelum {return_date}")
    input("Tekan Enter untuk melanjutkan...")
    book_menu()

# Fungsi untuk mengembalikan buku
def return_book():
    # Di sini Anda dapat menambahkan logika untuk mengembalikan buku dan
    # memperbarui data peminjaman di file JSON atau database.
    # Contoh sederhana:
    book_id = input("Masukkan ID buku yang ingin dikembalikan: ")

    print("\nBuku berhasil dikembalikan!")
    input("Tekan Enter untuk melanjutkan...")
    book_menu()

# Menjalankan aplikasi
if __name__ == "__main__":
    main_menu()
