class Stack:
	def __init__(self):
		self.items = []
	# Memeriksa apakah stack kosong
	def isEmpty(self):
		return self.items == []
	# Menambah objek/data ke dalam stack
	def push(self, item):
		self.items.append(item)
	# Mengeluarkan data dari stack
	def pop(self):
		return self.items.pop()
	# Menampilkan objek terakhir dari stack
	def peek(self):
		return self.items[len(self.items) - 1]
	# Menghitung panjang stack
	def size(self):
		return len(self.items)
	# Menu dari aplikasi
	def mainmenu(self):
		pilih = "y"
		while pilih == "y":
			print("=========================")
			print("| Menu aplikasi stack |")
			print("=========================")
			print("1. Push objek")
			print("2. Pop objek")
			print("3. Cek Empty")
			print("4. Tampil objek terakhir")
			print("5. Panjang dari stack")
			print("=========================")
			pilihan = str(input("Silakan masukan pilihan anda: "))
			if pilihan == "1":
				obj = str(input("Masukan objek yang ingin anda tambahkan: "))
				self.push(obj)
				print("Object " + obj + " telah ditambahkan")
				input("")
			elif pilihan == "2":
				print("Objek " + self.pop() + " dihapus")
				input("")
			elif pilihan == "3":
				print(self.isEmpty())
				input("")
			elif pilihan == "4":
				print("Objek terakhir: " + self.peek())
				input("")
			elif pilihan == "5":
				print("Panjang dari stack adalah: " + str(self.size()))
				input("")
			else:
				pilih = "n"


if __name__ == "__main__":
	s = Stack()
	s.mainmenu()