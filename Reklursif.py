def ganti_kata(teks, kata_cari, kata_ganti, index=0): 
    #string awal, kata yg dicari, kata yang diganti, indeks penanda urutan string
    if index >= len(teks): #kalau kondisi indeks sampai panjang teks
        return teks #cetak teksnya
    else: #selain itu
        if teks[index:index + len(kata_cari)] == kata_cari: 
            #kalau teks di indeks saat ini [X:X + panjang kata cari] = kata cari
            teks = teks[:index] + kata_ganti + teks[index + len(kata_cari):] 
            # maka bagian teks sebelum indeks pada indeks teks + kata ganti + teks setelah panjang kata ganti
        return ganti_kata(teks, kata_cari, kata_ganti, index + 1) #fungsi rekursif untuk pengulangan

teks = "Saya suka belajar Java. Java adalah bahasa pemrograman yang menyenangkan. Aku suka Java" 
#string yang diubah
print(f"\n{teks}") 
#print dulu teksnya
print(ganti_kata(teks, "Java", "Python")) 
#string awal, kata yg dicari, kata yang diganti, indeks penanda urutan string

#Dillon Christiano 2401010536
#Ngurah Putra Amerta Widhi 2401010508
#I Gusti bagus Indra Prasetya 2401010553