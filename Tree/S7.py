hs_table = [None] * 10
mhs = {
  'Asep',
  'Rafli',
  'Abyzar',
  'Charlie',
  'Budianto',
  'Diana',
}

def hash_func(val):
    return len(val) % 10

def add_data(val):
    index = hash_func(val)
    if hs_table[index] == None:
        hs_table[index] = []
    hs_table[index].append(val)

for m in mhs:
    add_data(m)
print(hs_table)

inp = input("Cari nama mahasiswa: ")

# #linear
# val = hash_func(inp)
# if hs_table[val] == inp:
#     print(f"{inp} ditemukan pada posisi {val}")
# else:
#     print("Key tidak ditemukan")

#linear search list inside list
val = hash_func(inp)
if inp in hs_table[val]:
    print(f"{inp} ditemukan pada posisi {val}")
else:
    print("Key tidak ditemukan")