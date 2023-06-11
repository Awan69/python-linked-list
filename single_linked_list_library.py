class Node:
    def __init__(self, visitor_name, book_title):
        self.visitor_name = visitor_name
        self.book_title = book_title
        self.next = None


class LibraryRecord:
    def __init__(self):
        self.head = None

    def add_record(self, visitor_name, book_title):
        new_record = Node(visitor_name, book_title)

        if self.head is None:
            self.head = new_record
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_record

    def print_records(self):
        if self.head is None:
            print("Tidak ada catatan peminjaman buku.")
        else:
            current = self.head
            visitor_records = {}
            while current is not None:
                visitor_name = current.visitor_name
                book_title = current.book_title

                if visitor_name not in visitor_records:
                    visitor_records[visitor_name] = [book_title]
                else:
                    visitor_records[visitor_name].append(book_title)

                current = current.next

            print("Daftar Buku yang Dipinjam:")
            for visitor_name, book_titles in visitor_records.items():
                print(f"Pengunjung: {visitor_name}")
                print("Buku yang Dipinjam:")
                for book_title in book_titles:
                    print(f"- {book_title}")
                print()


library_record = LibraryRecord()

while True:
    visitor_name = input(
        "Masukkan nama pengunjung (atau 'selesai' untuk keluar): ")
    if visitor_name == "selesai":
        break

    book_title = input("Masukkan judul buku yang dipinjam: ")
    library_record.add_record(visitor_name, book_title)

library_record.print_records()
