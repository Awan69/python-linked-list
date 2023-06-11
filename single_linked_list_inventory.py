class Node:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None


class InventoryManagement:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Node(name, code, stock)

        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        if self.head is None:
            return

        if self.head.code == code:
            self.head = self.head.next
            return

        current = self.head
        prev = None

        while current is not None and current.code != code:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def print_inventory(self):
        if self.head is None:
            print("Daftar produk kosong.")
        else:
            current = self.head
            print("Daftar Produk:")
            while current is not None:
                print(
                    f"Nama: {current.name} | Kode: {current.code} | Stok: {current.stock}")
                current = current.next


inventory = InventoryManagement()

# Menambahkan produk baru ke dalam inventaris
while True:
    name = input("Masukkan nama produk (atau 'selesai' untuk keluar): ")
    if name == "selesai":
        break

    code = input("Masukkan kode produk: ")
    stock = int(input("Masukkan jumlah stok produk: "))
    inventory.add_product(name, code, stock)

# Mencetak daftar produk dalam inventaris
inventory.print_inventory()

# Menghapus produk dari inventaris
while True:
    code = input(
        "Masukkan kode produk yang akan dihapus (atau 'selesai' untuk keluar): ")
    if code == "selesai":
        break

    inventory.remove_product(code)

# Mencetak daftar produk setelah penghapusan
inventory.print_inventory()
