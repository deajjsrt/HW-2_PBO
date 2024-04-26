class Penilaian:
    def _init_(self, nama_mahasiswa):
        self.nama_mahasiswa = nama_mahasiswa
        self.nilai_tugas = 0
        self.nilai_quiz = 0
        self.nilai_ujian = 0

    def input_nilai(self):

        self.nilai_tugas = float(input("Masukkan nilai tugas: "))
        self.nilai_quiz = float(input("Masukkan nilai quiz: "))
        self.nilai_ujian = float(input("Masukkan nilai ujian: "))

    def hitung_nilai_akhir(self):

        nilai_akhir = (self.nilai_tugas * 0.3) + (self.nilai_quiz * 0.2) + (self.nilai_ujian * 0.5)
        return nilai_akhir

nama_mahasiswa = input("Masukkan nama mahasiswa: ")
penilaian_mahasiswa = Penilaian(nama_mahasiswa)

penilaian_mahasiswa.input_nilai()

nilai_akhir = penilaian_mahasiswa.hitung_nilai_akhir()