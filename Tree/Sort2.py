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

# def merge_sort(ls):
#     mid = len(ls) // 2
#     left_half = merge_sort(ls[:mid])
#     right_half = merge_sort(ls[mid:])
#     merge(left_half, right_half)
    
#     print(left_half, right_half)

# def merge(left, right):
#     result = []
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#         print(i, j, result)

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

ls = [1, 7, 2, 5, 10, 3, 4, 6, 8, 9]
X = quick_sort(ls)
print(X)
