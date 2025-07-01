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
    {"nim": 11019, "nama": "Lolita"},
    {"nim": 11020, "nama": "Spark Baster"},
]

A = input("Masukan Nama: ")
i = 0
while i < len(Nama):
    for i in range(len(Nama)):
        if A == A in Nama[i]["nama"]:
            print(f"{A} ditemukan pada posisi {i} dengan nim {Nama[i]['nim']}")
        else:
            continue
    else:
        print("Key tidak ditemukan")   