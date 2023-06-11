class Node:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.next = None


class Tournament:
    def __init__(self):
        self.head = None

    def register_player(self, name, ranking):
        new_player = Node(name, ranking)

        if self.head is None:
            self.head = new_player
        else:
            current = self.head
            prev = None
            while current is not None and current.ranking < new_player.ranking:
                prev = current
                current = current.next

            if prev is None:
                new_player.next = self.head
                self.head = new_player
            else:
                prev.next = new_player
                new_player.next = current

    def eliminate_player(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        current = self.head
        prev = None

        while current is not None and current.name != name:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def print_players(self):
        if self.head is None:
            print("Daftar peserta kosong.")
        else:
            current = self.head
            print("Daftar Peserta:")
            while current is not None:
                print(f"Nama: {current.name} | Peringkat: {current.ranking}")
                current = current.next


tournament = Tournament()

while True:
    name = input("Masukkan nama peserta (atau 'selesai' untuk keluar): ")
    if name == "selesai":
        break

    ranking = int(input("Masukkan peringkat peserta: "))
    tournament.register_player(name, ranking)

tournament.print_players()

while True:
    name = input(
        "Masukkan nama peserta yang kalah (atau 'selesai' untuk keluar): ")
    if name == "selesai":
        break

    tournament.eliminate_player(name)

tournament.print_players()
