class Mahasiswa:
    def __init__(self, nim, password):
        self.nim = nim
        self.password = password
        self.logged_in = False

    def login(self, username, password):
        if self.nim == username and self.password == password:
            self.logged_in = True
            print("Login berhasil untuk mahasiswa dengan NIM:", self.nim)
        else:
            print("Login gagal. NIM atau kata sandi salah.")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("Logout berhasil.")
        else:
            print("Tidak ada yang login saat ini.")

mahasiswa1 = Mahasiswa("422023017", "password123")

mahasiswa1.login("422023017", "password123")

mahasiswa1.logout()