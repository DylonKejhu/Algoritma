# import operator as op

def bubble(ls):
    for i in range(len(ls)):
        for j in range(0, len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
        print("Langkah ke-", i+1, ":", ls)
    return ls

def insertion(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while j >= 0 and key < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
        print("Langkah ke-", i, ":", ls)
    return ls

def selection(ls):
    for i, l in enumerate(ls):
        min_value = l
        min_index = i

        # print(i, l)
        
        for j, k in enumerate(ls[i:]):
            if k < min_value:
                min_value = k
                min_index = j + i
        ls[i], ls[min_index] = ls[min_index], ls[i]

        print(i, min_index, ls[i], ls[min_index])
    return  ls

def merge_sort(ls):
    if len(ls) > 1:
        mid = len(ls) // 2
        left_half = merge_sort(ls[:mid])
        right_half = merge_sort(ls[mid:])
        merged_list = merge(left_half, right_half)
    else:
        return ls
    return merged_list

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def quick_sort(ls):
    pivot = ls[-1]
    left = []
    right = []

    for i, l in enumerate(ls[:-1]):
        if l < pivot:
            left.append(l)
        else:
            right.append(l)
    
    print("pivot", pivot)
    print("left", left)
    print("right", right)

    if len(left) > 1:
        left = quick_sort(left)
    if len(right) > 1:
        right = quick_sort(right)

    return left + [pivot] + right

n = int(input("Berapa banyak angka yang ingin dimasukkan? "))
ls = []
for i in range(n):
    x = int(input(f"Masukkan angka ke-{i+1}: "))
    ls.append(x)

print("\nPilih metode sorting:")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Built-in Sort (sorted())")
print("4. Selection Sort")
print("5. Merge Sort")
print("6. Quick Sort")

pilihan = input("Pilihan (1/2/3/4/5/6): ")

if pilihan == '1':
    print("\nProses Bubble Sort:")
    bubble(ls)
elif pilihan == '2':
    print("\nProses Insertion Sort:")
    insertion(ls)
elif pilihan == '3':
    print("\nHasil Built-in Sort:")
    print(sorted(ls))
elif pilihan == '4':
    print("\nProses Selection Sort:")
    selection(ls)
elif pilihan == '5':
    print("\nProses Merge Sort:")
    merge_sort(ls)
elif pilihan == '6':
    print("\nProses Quick Sort:")
    quick_sort(ls)
else:
    print("Pilihan tidak valid.")