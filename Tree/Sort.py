import operator

# lsNilai.sort()
# print(lsNilai)

# lsMhs = [
#     {"nim": "123", "nama": "A"},
#     {"nim": "456", "nama": "B"},
#     {"nim": "789", "nama": "C"},
#     {"nim": "101", "nama": "D"},
#     {"nim": "234", "nama": "E"},
# ]

# lsMhs.sort(key=operator.itemgetter("nama"))
# print(lsMhs)



# lsNilai = [5, 4, 3, 2, 1, 7, 6, 8, 9]
# def insertion(lsNilai):
#     newLs = []

#     for index_ls, value_ls in enumerate(lsNilai):
#         print(index_ls, value_ls)
#         if len(newLs) == 0:
#             newLs.append(value_ls)
#         else:
#             for index_newLs, value_newLs in enumerate(newLs):
#                 if value_newLs < value_ls:
#                     newLs.insert(index_newLs, value_ls)
#                     break
#                 elif value_newLs == value_ls:
#                     newLs.append(value_ls)
#                     break

#     return newLs

# insertion(lsNilai)

def insertionSingle(ls):
    for index_ls, value_ls in enumerate(ls):
        if index_ls == 0:
            continue
            for i in range(index_ls, 0, -1):
                if ls[i] < ls[i-1]:
                    ls[i], ls[i-1] = ls[i-1], ls[i]
                else:
                    break
            print(ls)
    return ls


X = [5, 4, 3, 2, 1, 7, 6, 8, 9]
insertionSingle(X)

def bubble(ls):
    for i in range(len(ls)):
        for j in range(0, len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
        print(ls)
    
bubble(X)

