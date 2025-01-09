def Jasuke(Jagung, SKM, Keju, Gula, Garam, Mentega):
    print(f"\nBahan dalam produk anda :\n"
          f"{Jagung} buah Jagung\n"
          f"{SKM} ml SKM\n"
          f"{Keju} gram Keju\n"
          f"{Gula} sdm Gula\n"
          f"{Garam} sdt Garam\n"
          f"{Mentega} sdt Mentega\n")
    
    if 2 <= Jagung <= 3:
        print("Jagungnya Pas !")
    elif Jagung < 2:
        print("jagungnya Kurang !")
    elif Jagung > 3:
        print("jagungnya Kelebihan ! !")
         
    if 150 <= SKM <= 250:
        print("SKM Pas !")
    elif SKM < 150:
        print("SKM Kurang !")
    elif SKM > 250:
        print("SKM Kelebihan ! !")
    
    if 75 <= Keju <= 125:
        print("Keju Pas !")
    elif Keju < 75:
        print("Keju Kurang !")
    elif Keju > 125:
        print("Keju Kelebihan ! !")
        
    if 2 <= Gula <= 3:
        print("Gula Pas !")
    elif Gula < 2:
        print("Gula Kurang !")
    elif Gula > 3:
        print("Gula Kelebihan ! !")
        
    if 1 <= Garam <= 2:
        print("Garam Pas !")
    elif Garam < 1:
        print("Garam Kurang !")
    elif Garam > 2:
        print("Garam Kelebihan ! !")
    
    if Mentega == 1:
        print("Mentega Pas !")
    elif Mentega < 1:
        print("Mentega Kurang !")
    elif Mentega > 1:
        print("Mentega Kelebihan ! !")
        

A = int(input("Masukan Jagung (Buah) : "))
B = int(input("Masukan SKM (ml) : "))
C = int(input("Masukan Keju (gram) : "))
D = int(input("Masukan Gula (sdm) : "))
E = int(input("Masukan Garam (sdt) : "))
F = int(input("Masukan Mentega (sdt) : "))
Jasuke(A, B, C, D, E, F)