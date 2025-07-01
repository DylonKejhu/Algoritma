Nama = [
    {"nim": 11010, "nama": "John Mary"},
    {"nim": 11011, "nama": "John Peter"},
    {"nim": 11012, "nama": "John Paul"},
    {"nim": 11013, "nama": "John Rawr"},
    {"nim": 11014, "nama": "John Dork"},
    {"nim": 11015, "nama": "John Spock"},
    {"nim": 11016, "nama": "John Mama"},
    {"nim": 11017, "nama": "John Don"},
    {"nim": 11018, "nama": "John Man"},
]

A = int(input("Masukan nim: "))

for i in range(len(Nama)):
    if A == Nama[i]["nim"]:
        print(f"{A} ditemukan pada posisi {i} dengan nama {Nama[i]['nama']}")
        break
else:
    print("Key tidak ditemukan")

for index, value in enumerate(Nama):
    if A == value["nim"]:
        print(f"{A} ditemukan pada posisi {index} dengan nama {value['nama']}")
        break
else:
    print("Key tidak ditemukan")