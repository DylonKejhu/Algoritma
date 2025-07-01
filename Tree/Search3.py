X = [1, 4, 2, 9, 5, 7, 3, 6, 8]
X.sort()

start = 0
end = len(X) - 1

A = int(input("Masukan Angka: "))

found = False
while not found:
    mid = start + end // 2
    if X[mid] == A:
        print(f"{A} found at position {mid}")
        found = True
    elif X[mid] > A:
        end = mid - 1
    else:
        start = mid + 1
