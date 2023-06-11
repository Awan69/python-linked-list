class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Node(description, priority)

        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            prev = None
            while current is not None and current.priority >= new_task.priority:
                prev = current
                current = current.next

            if prev is None:
                new_task.next = self.head
                self.head = new_task
            else:
                prev.next = new_task
                new_task.next = current

    def remove_task(self, description):
        if self.head is None:
            return

        if self.head.description == description:
            self.head = self.head.next
            return

        current = self.head
        prev = None

        while current is not None and current.description != description:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def print_tasks(self):
        if self.head is None:
            print("Tidak ada tugas dalam daftar.")
        else:
            current = self.head
            print("Daftar Tugas:")
            while current is not None:
                print(
                    f"Deskripsi: {current.description} | Prioritas: {current.priority}")
                current = current.next


task_list = TaskList()

while True:
    description = input(
        "Masukkan deskripsi tugas (atau 'selesai' untuk keluar): ")
    if description == "selesai":
        break

    priority = int(input("Masukkan prioritas tugas (1-5): "))
    task_list.add_task(description, priority)

task_list.print_tasks()

while True:
    description = input(
        "Masukkan deskripsi tugas yang ingin dihapus (atau 'selesai' untuk keluar): ")
    if description == "selesai":
        break

    task_list.remove_task(description)

task_list.print_tasks()
