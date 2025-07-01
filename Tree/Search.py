X = [1, 4, 2, 9, 5, 7, 3, 6, 8]

# A =  int(input("Masukan Angka: "))
# if A in X:
#     print(f"{A} found at position {X.index(A)}")
# else:
#     print("Angka tidak ditemukan")

A = int(input("Masukan Angka: "))

for i in range(len(X)):
    if A == X[i]:
        print(f"{A} found at position {i}")
        break
else:
    print("Key tidak ditemukan")

for i, v in enumerate(X):
    if A == v:
        print(f"{A} found at position {i}")
        break
else:
    print("Key tidak ditemukan")