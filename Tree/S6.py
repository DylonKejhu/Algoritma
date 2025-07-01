import hashlib

password = 'Rawr'
hashed_password = hashlib.md5(password.encode()).hexdigest()
print(hashed_password)

usr_input = input("Masukan password: ")
hashed_input = hashlib.md5(usr_input.encode()).hexdigest()

if hashed_input == hashed_password:
    print("Password valid")
else:
    print("Password tidak valid")


