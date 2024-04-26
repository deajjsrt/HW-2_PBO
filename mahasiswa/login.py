class Mahasiswa:
    def __init__(self, nim, password):
        self.nim = nim
        self.password = password

    def login(self, username, password):
        if self.nim == username and self.password == password:
            return True
        else:
            return False

mahasiswa1 = Mahasiswa("422023017", "ukrida123")

username_input = input("Masukkan NIM: ")
password_input = input("Masukkan kata sandi: ")

if mahasiswa1.login(username_input, password_input):
    print("Login berhasil!")
else:
    print("Login gagal. NIM atau kata sandi salah.")
