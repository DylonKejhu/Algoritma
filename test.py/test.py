import time

jumlah_ayam = ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh"]

with open("hasil_anak_ayam.txt", "w") as file:
    print("\nTek kotek kotek kotek\n"
          "Anak ayam turun berkotek\n"
          "Tek kotek kotek kotek\n"
          "Anak ayam turun berkotek", file=file)

    for ayam in reversed(jumlah_ayam):
        print(f"\nAnak ayam turunlah {ayam}", file=file)
        if ayam != "satu":
            print(f"Mati satu tinggal {jumlah_ayam[jumlah_ayam.index(ayam) - 1]}", file=file)
        else:
            print("Mati satu tinggal induknya\n", file=file)
        time.sleep(0.5)
