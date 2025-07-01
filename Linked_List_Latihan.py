# Class Node
class Node:
    # Inisialisasi node
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Class untuk Doubly Linked List
class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Menambah node
    def menuTambah(self):
        temp = int(input('Masukkan data baru = '))
        new_node = Node(temp)

        # Memeriksa apakah list kosong
        if self.head is None:
            # Menunjuk HEAD dan TAIL ke node baru
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Menghapus node
    def menuHapus(self):
        temp = int(input('Masukkan data yang akan dihapus = '))

        # Membuat pointer yang menunjuk ke node pertama
        current_node = self.head

        # Melakukan perulangan saat list tidak kosong
        while current_node is not None:
            if current_node.data == temp:
                # Jika node yang dicari berada pada elemen terakhir
                if current_node.next is None:
                    if current_node.prev:
                        current_node.prev.next = None
                        self.tail = current_node.prev
                    else:
                        self.head = self.tail = None
                # Jika node yang dicari berada di tengah
                elif current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                # Jika node yang dicari berada pada elemen pertama
                else:
                    self.head = current_node.next
                    if self.head:
                        self.head.prev = None
                return
            current_node = current_node.next

        print("Data tidak ditemukan.")

    # Menampilkan isi dari list
    def menuTampil(self):
        print("Tampilkan list data:")
        current_node = self.head

        # Menampilkan data beserta data sebelum dan sesudahnya
        while current_node is not None:
            prev_data = current_node.prev.data if current_node.prev else None
            next_data = current_node.next.data if current_node.next else None
            print(f"Prev: {prev_data} | Data: {current_node.data} | Next: {next_data}")
            current_node = current_node.next

    # Menampilkan menu program
    def menuUmum(self):
        while True:
            print("\nPilih menu yang anda inginkan")
            print("==============================")
            print("1 : Tambah data ke linked list")
            print("2 : Hapus data di linked list")
            print("3 : Tampilkan data di linked list")
            print("4 : Keluar Program")
            pilihan = input("Masukkan Menu yang anda pilih = ")

            if pilihan == "1":
                self.menuTambah()
            elif pilihan == "2":
                self.menuHapus()
            elif pilihan == "3":
                self.menuTampil()
            elif pilihan == "4":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid.")


                
if __name__ == "__main__":
    d = DoubleList()
    d.menuUmum()
