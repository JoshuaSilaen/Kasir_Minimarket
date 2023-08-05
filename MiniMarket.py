# Dictionary untuk menyimpan data item
data_item = {
    "A001": {"Nama": "Air Mineral", "Harga": 5000, "Stock": 50},
    "A002": {"Nama": "Keripik Kentang", "Harga": 10000, "Stock": 30},
    "A003": {"Nama": "Roti Sobek", "Harga": 15000, "Stock": 40},
    "A004": {"Nama": "Kopi Botol", "Harga": 8000, "Stock": 20},
}

# Fungsi untuk melihat stock item
def lihat_stock():
    print("===== Stock Item Minimarket =====")
    print("{:<10} {:<15} {:<10} {:<10}".format("Kode Item", "Nama Item", "Harga", "Stock"))
    for kode, item in data_item.items():
        print("{:<10} {:<15} {:<10} {:<10}".format(kode, item["Nama"], item["Harga"], item["Stock"]))

# Fungsi untuk menambah stock item
def tambah_stock():
    print("===== Tambah Stock Item =====")
    nama_item = input("Masukkan nama item: ")
    harga = int(input("Masukkan harga: "))
    stock = int(input("Masukkan stock tersedia: "))

    # Generate kode item baru
    kode_item = "A" + str(len(data_item) + 1).zfill(3)

    data_item[kode_item] = {
        "Nama": nama_item,
        "Harga": harga,
        "Stock": stock
    }
    print("Item berhasil ditambahkan!")

# Fungsi untuk melakukan transaksi
def transaksi():
    print("===== Transaksi Minimarket =====")
    lihat_stock()
    kode_item = input("Masukkan kode item yang ingin dibeli: ")
    qty = int(input("Masukkan jumlah yang ingin dibeli: "))

    item = data_item.get(kode_item)

    if item is None:
        print("Item dengan kode tersebut tidak ditemukan.")
    else:
        available_stock = item["Stock"]
        if qty > available_stock:
            print("Stock tidak mencukupi untuk transaksi.")
        else:
            total_harga = item["Harga"] * qty
            print(f"Total harga: {total_harga}")
            data_item[kode_item]["Stock"] = available_stock - qty
            print("Transaksi berhasil!")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    while True:
        print("\n===== Menu Minimarket =====")
        print("1. Lihat Stock Item")
        print("2. Tambah Stock Item")
        print("3. Transaksi")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/0): ")

        if pilihan == '1':
            lihat_stock()
        elif pilihan == '2':
            tambah_stock()
        elif pilihan == '3':
            transaksi()
        elif pilihan == '0':
            print("Terima kasih. Program berakhir.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    tampilkan_menu()
