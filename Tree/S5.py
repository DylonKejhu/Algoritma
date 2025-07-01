mhs = {
  '101010': {
    'nama': 'Andini',   
    'prodi':'Informatika'
  },
  '101011': {
    'nama': 'Belinda', 
    'prodi':'Informatika'
  },
  '101012': {
    'nama': 'Cindy', 
    'prodi':'Informatika'
  },
  '101013': {
    'nama': 'Denny', 
    'prodi':'Informatika'
  },
}

search = input("Masukan nama: ")

if search in mhs:
    print(f"{search} ditemukan pada posisi {mhs[search]['nama']} dengan prodi {mhs[search]['prodi']}")
else:
    print("Key tidak ditemukan")
