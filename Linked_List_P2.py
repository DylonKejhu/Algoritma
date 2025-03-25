# Membuat class untuk node
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # Mengambil data dari node
    def get_data(self):
        return self.data
    
    # Mengambil node berikutnya
    def get_next(self):
        return self.next_node
    
    # Menentukan node berikutnya
    def set_next(self, new_next):
        self.next_node = new_next

# Membuat class untuk linked list
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Menambah node baru
    def insert(self, data):
        # Inisialisasi node baru
        new_node = Node(data)
        # Menunjuk node berikutnya dari node baru ke node yang ditunjuk oleh HEAD
        new_node.set_next(self.head)
        # HEAD menunjuk ke node baru
        self.head = new_node

    # Menghitung panjang list
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count  # Kesalahan sebelumnya ada di return dalam loop, harusnya di luar

    # Mencari sebuah data pada list
    def search(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    # Menghapus node
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Data tidak ditemukan dalam list")

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # Menampilkan isi dari list
    def showData(self):
        print("Tampilkan list data:")
        print("Node -> Next Node")
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            if current_node.next_node:
                print(current_node.next_node.data)
            else:
                print("None")
            current_node = current_node.next_node

    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while pilih.lower() == "y":
            print("===============================")
            print("|    Menu aplikasi linked list   |")
            print("===============================")
            print("1. Insert data")
            print("2. Delete data")
            print("3. Cari data")
            print("4. Panjang dari linked list")
            print("5. Tampil data")
            print("6. Keluar")
            print("===============================")
            pilihan = input("Silakan masukan pilihan anda: ")

            if pilihan == "1":
                obj = input("Masukan data yang ingin ditambahkan: ")
                self.insert(obj)
            elif pilihan == "2":
                obj = input("Masukan data yang ingin dihapus: ")
                try:
                    self.delete(obj)
                    print("Data berhasil dihapus")
                except ValueError as e:
                    print(e)
            elif pilihan == "3":
                obj = input("Masukan data yang ingin dicari: ")
                status = self.search(obj)
                if status:
                    print("Data ditemukan dalam list")
                else:
                    print("Data tidak ditemukan")
            elif pilihan == "4":
                print("Panjang dari linked list adalah:", self.size())
            elif pilihan == "5":
                self.showData()
            elif pilihan == "6":
                print("Keluar dari program")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    # Menjalankan program utama
    l = LinkedList()
    l.mainmenu()
