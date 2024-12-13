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
    #Suhu awal -> Konversi ke C -> Konversi tujuan suhu
    celcius = suhu
    fahrenheit = (9/5 * suhu) + 32
    kelvin = celcius + 273.15
    reimur = 4/5 * suhu

    suhu = float(input("Masukan suhu anda\n"))
    unitawal = input("Masukan unit suhu anda\n(C, F, K, R)\n").lower()
    unitakhir = input("Konversi ke mana ?\n(C, F, K, R)\n").lower()

    if unitawal == "c":
        print
    elif unitawal == "f":
        print
    elif unitawal == "k":
        print
    elif unitawal == "r":
        print
    else:
        print

rawr = input("\nPilih Kalkulatornya :\n1. Kalkulator Biasa\n2. Kalkulator Pengecek Angka Genap atau Ganjil\n3. Pengecek huruf vokal dan konsonan\n4. Pengecek suhu\n")
if rawr == "1":
    kalkulator()
elif rawr == "2":
    pengecekangka()
elif rawr == "3":
    vokalkonsonan()
elif rawr == "4":
    konversisuhu()
else:
    print("Pilihan anda tidak valid. Silakan coba lagi yaa.")
