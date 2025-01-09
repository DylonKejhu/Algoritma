import time

jumlah_ayam = ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh"]

print("\nTek kotek kotek kotek\n"
          "Anak ayam turun berkotek\n"
          "Tek kotek kotek kotek\n"
          "Anak ayam turun berkotek")

for ayam in reversed(jumlah_ayam):
    print(f"\nAnak ayam turunlah {ayam}")
    if ayam != "satu":
        print(f"Mati satu tinggal {jumlah_ayam[jumlah_ayam.index(ayam) - 1]}")
    else:
        print("Mati satu tinggal induknya\n")
    time.sleep(0.5)

# jumlah = 10
# for ayam in range(jumlah):
#     print(f"\nAnak ayam turunlah {jumlah}")
#     jumlah -= 1
#     if jumlah >= 1:
#         print(f"Mati Satu tinggal {jumlah}")
#     elif jumlah == 0:
#         print("Mati Satu tinggal Induknya\n")
#     time.sleep(0.5)