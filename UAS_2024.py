#Dillon Christiano
#2401010536


Banyak_Data = int(input("\nBanyak data ? "))  # memasukan banyaknya data yang ada
Data = [] #definisi list python
for nambah in range(Banyak_Data): # pengulangan for sebanyak range function yang berisi variabel dari inputan integer Banyak_Data
    Data.append(int(input(f"Data ke {nambah + 1}: "))) # function append untuk menambahkan data
Rata = sum(Data) / len(Data) # Kalkulasi Rata Rata
print(f"Jumlah Data: {sum(Data)}" # sum jumlah data
      f"\nBanyak Data:{len(Data)}" # lenght panajng data
      f"\nRata Rata: {Rata}") # memanggil variabel Rata

Limit = int(input("Masukan batas atas angka yang habis dibagi 3\n")) # Input angkanya
Angka = 1 # dimulai dari 1 karena apapun yang dibagi 0 maka akan hasilnya 0
while Angka <= Limit: # disaat angkanya kurang dari cek sama dengan integer dari variabel Limit
    if Angka % 3 == 0: # kalau angka di "%" dengan 3 menghasilkan cek 0 
        print(f"{Angka}") # print integer variabel angkanya
    Angka += 1 # nambah operasi +1 di variabel Angka sampai <= Limit