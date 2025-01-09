def kalkulator():
    print("Kalkulator simpel \nSilahkan ikuti petunjuk untuk mengoperasikan kalkulator")

    x = float(input("Input angka pertama:\n"))
    y = float(input("Input angka kedua:\n"))
    op = input("Operasi apa yang ingin dilakukan \nPilih operasi:\n(+, -, *, /)\n")

    if op == "+":
        print("Hasilnya adalah... ", x + y)
    elif op == "-":
        print("Hasilnya adalah... ", x - y)
    elif op == "*":
        print("Hasilnya adalah... ", x * y)
    elif op == "/":
        print("Hasilnya adalah... ", x / y)
    else:
        print("Bilangan bukan angka atau operasi tidak dikenal.")
def pengecekangka():
    print("Kalkulator Simpel Ganjil / Genap \nMenentukan apakah angka yang diinput genap atau ganjil")
    x = int(input("Input angka yang ingin dicek:\n"))

    if x % 2 != 0:
        print("Angka", x, "adalah angka ganjil")
    elif x % 2 == 0:
        print("Angka", x, "adalah angka genap")
    else:
        print("Bilangan bukan angka.")
def vokalkonsonan():
    x = input("Pengecek vokal dalam alfabet\nMasukan huruf yang akan dicek:\n").upper()
    if len(x) == 1:
        if x.isalpha():
            if x in "AIUEO":
                print("Huruf", x, "adalah vokal")
            else:
                print("Huruf", x, "adalah konsonan")
        elif x.isdigit():
            print("Anda memasukan", x, "sebagai angka")
        else:
            print("Simbol", x, "bukanlah alfabet")
    else:
        print("Input", x, "terbilang lebih dari 1 digit, mohon ulangi operasi lagi")
def konversisuhu():
    suhuawal = float(input("Masukan suhu anda\n"))
    unitawal = input("Masukan unit suhu anda\n(C, F, K, R)\n").upper()
    unitakhir = input("Konversi ke mana ?\n(C, F, K, R)\n").upper()

    if unitawal == "C":
        suhu = suhuawal
    elif unitawal == "F":
        suhu = (suhuawal - 32) * 5/9  
    elif unitawal == "K":
        suhu = suhuawal - 273.15
    elif unitawal == "R":
        suhu = suhuawal * 5/4 
    elif unitawal == "RA":
        suhu = (suhuawal - 491.67) * 5/9

    if unitakhir == "C":
        suhuakhir = suhu
    elif unitakhir == "F":
        suhuakhir = (suhu * 9/5) + 32
    elif unitakhir == "K":
        suhuakhir = suhu + 273.15
    elif unitakhir == "R":
        suhuakhir = suhu * 4/5
    elif unitakhir == "RA":
        suhuakhir = (suhu * 9/5) + 491.67

    print(f"Suhu adalah {suhuakhir}")
def looping():
    for i in range(100):
        if i == 100:
            break  # Stop the loop when i is 5
        if i % 2 == 0:
            continue  # Skip even numbers
    print(i)

rawr = input("\nPilih Kalkulatornya :\n1. Kalkulator Biasa\n2. Kalkulator Pengecek Angka Genap atau Ganjil\n3. Pengecek huruf vokal dan konsonan\n4. Pengecek suhu\n")
if rawr == "1":
    kalkulator()
elif rawr == "2":
    pengecekangka()
elif rawr == "3":
    vokalkonsonan()
elif rawr == "4":
    konversisuhu()
elif rawr == "5":
    looping()
else:
    print("Pilihan anda tidak valid. Silakan coba lagi yaa.")
