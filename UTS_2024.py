def Cek_Kelulusan():
    print("Input Nilai Anda\n")
    Nilai_Tugas = float(input("Nilai Tugas = "))
    Nilai_Kuis = float(input("Nilai Kuis = "))
    Nilai_UTS = float(input("Nilai UTS = "))
    Nilai_UAS = float(input("Nilai UAS = "))
    Kehadiran = float(input("Kehadiran = "))
    Nilai_Rata = (Nilai_Tugas + Nilai_Kuis + Nilai_UTS + Nilai_UAS)/4
    if Nilai_Rata >= 60 and Kehadiran >= 12:
        Output = print(f"Selamat Anda LULUS dengan nilai {Nilai_Rata}")
    else:
        Output = print("Maaf Anda Tidak LULUS")

def Konversi_Nilai_Ke_Huruf():
    Nilai = float(input("Masukan Input Nilai Anda\n"))
    if 81 <= Nilai <= 100:
        Nilai_Huruf = "A"
    elif 61 <= Nilai <= 80:
        Nilai_Huruf = "B"
    elif 41 <= Nilai <= 60:
        Nilai_Huruf = "C"
    elif 21 <= Nilai <= 40:
        Nilai_Huruf = "D"
    elif 0 <= Nilai <= 20:
        Nilai_Huruf = "E"
    else:
        Nilai_Huruf = "tidak valid"
    print(f"Nilai anda adalah {Nilai_Huruf} ({Nilai})")

print("Proses... ")
Pilihan = input("\nDillon Christiano - 2401010536 - UTS Algoritma"
                "\n1. Cek Kelulusan"
                "\n2. Konversi Nilai Ke Huruf\n")
if Pilihan == "1":
    Cek_Kelulusan()
elif Pilihan == "2":
    Konversi_Nilai_Ke_Huruf()