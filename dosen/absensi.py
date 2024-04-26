class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class MataKuliah:
    def __init__(self, nama_mk, kode_mk):
        self.nama_mk = nama_mk
        self.kode_mk = kode_mk
        self.daftar_absensi = []

    def absen(self, mahasiswa):
        self.daftar_absensi.append(mahasiswa)

    def tampilkan_absensi(self):
        print("Daftar Mahasiswa yang Hadir pada Mata Kuliah", self.nama_mk)
        for mahasiswa in self.daftar_absensi:
            print("- Nama:", mahasiswa.nama, "| NIM:", mahasiswa.nim)

mahasiswa1 = Mahasiswa("Yonathan Dea", "422023017")
mahasiswa2 = Mahasiswa("Clara Elisa", "422023018")

mata_kuliah_pbo = MataKuliah("Pemrograman Berorientasi Objek", "PB01")

mata_kuliah_pbo.absen(mahasiswa1)
mata_kuliah_pbo.absen(mahasiswa2)

mata_kuliah_pbo.tampilkan_absensi()