class Mahasiswa:
    def __init__(self, nama_lengkap, alamat, tanggal_lahir, email, password):
        self.nama_lengkap = nama_lengkap
        self.alamat = alamat
        self.tanggal_lahir = tanggal_lahir
        self.email = email
        self.password = password

    def daftar(self):

        print("Pendaftaran berhasil untuk mahasiswa dengan nama:", self.nama_lengkap)

nama_lengkap = input("Masukkan nama lengkap: ")
alamat = input("Masukkan alamat: ")
tanggal_lahir = input("Masukkan tanggal lahir (DD-MM-YYYY): ")
email = input("Masukkan email: ")
password = input("Masukkan kata sandi: ")

mahasiswa_baru = Mahasiswa(nama_lengkap, alamat, tanggal_lahir, email, password)

mahasiswa_baru.daftar()