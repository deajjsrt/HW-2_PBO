class SumberDayaAkademik:
    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi

    def tampilkan_info(self):
        print("Nama Sumber Daya Akademik:", self.nama)
        print("Deskripsi:", self.deskripsi)

sumber_daya1 = SumberDayaAkademik("Perpustakaan", "Tempat untuk meminjam buku dan sumber referensi lainnya.")
sumber_daya2 = SumberDayaAkademik("Laboratorium Komputer", "Tempat untuk praktikum dan eksperimen di bidang komputer.")

print("Informasi Sumber Daya Akademik:")
print("------------------------------")
sumber_daya1.tampilkan_info()
print("\n")
sumber_daya2.tampilkan_info()