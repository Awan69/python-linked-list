class Node:
    def __init__(self, item_name, importance_level):
        self.item_name = item_name
        self.importance_level = importance_level
        self.next = None


class Inventory:
    def __init__(self):
        self.head = None

    def add_item(self, item_name, importance_level):
        new_item = Node(item_name, importance_level)

        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            prev = None
            while current is not None and current.importance_level >= new_item.importance_level:
                prev = current
                current = current.next

            if prev is None:
                new_item.next = self.head
                self.head = new_item
            else:
                prev.next = new_item
                new_item.next = current

    def remove_item(self, item_name):
        if self.head is None:
            return

        if self.head.item_name == item_name:
            self.head = self.head.next
            return

        current = self.head
        prev = None

        while current is not None and current.item_name != item_name:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def print_inventory(self):
        if self.head is None:
            print("Tas kosong.")
        else:
            current = self.head
            print("Daftar Item dalam Tas:")
            while current is not None:
                print(
                    f"Nama: {current.item_name} | Tingkat Kepentingan: {current.importance_level}")
                current = current.next


inventory = Inventory()

while True:
    item_name = input("Masukkan nama item (atau 'selesai' untuk keluar): ")
    if item_name == "selesai":
        break

    importance_level = int(input("Masukkan tingkat kepentingan item (1-5): "))
    inventory.add_item(item_name, importance_level)

inventory.print_inventory()

while True:
    item_name = input(
        "Masukkan nama item yang ingin dihapus (atau 'selesai' untuk keluar): ")
    if item_name == "selesai":
        break

    inventory.remove_item(item_name)

inventory.print_inventory()
