class buku:
    def __init__(self, judul, penulis, stok):
        self.judul = judul
        self.penulis = penulis
        self.stok = stok
        self.status = "Tersedia"  

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Stok: {self.stok}")
        print(f"Status: {self.status}")
        print("-" * 30)
        
    def cek_ketersediaan(self):
        return self.status == "Tersedia" and self.stok > 0

class anggota:
    def __init__(self, nama, NIM, semester):
        self.nama = nama
        self.NIM = NIM
        self.semester = semester
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if buku.status == "Tersedia" and buku.stok > 0: 
            buku.status = "dipinjam"
            buku.stok -= 1
            self.buku_dipinjam= buku
            print(f"{self.nama} berhasil meminjam buku {buku.judul}")
        else: 
            print(f"maaf, buku {buku.judul} sedang tidak tersedia untuk dipinjam saat ini. datang kembali nanti😊")
    
    def kembalikan_buku(self):
        if self.buku_dipinjam:
            buku = self.buku_dipinjam
            buku.status = "tersedia" 
            buku.stok += 1
            self.buku_dipinjam = []
            print(f"{self.nama} terima kasih, telah mengembalikan buku ini {buku.judul}")
        else:
            print("anda tidak meminjam buku apapun.")

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.NIM}")
        print(f"Semester: {self.semester}")
        if self.buku_dipinjam:
            print("Buku yang dipinjam:")
            self.buku_dipinjam.tampilkan_info()
        else:
            print("Tidak ada buku yang dipinjam.")
        print("-" * 30)

class perpustakaan:
    def __init__(self, nama_pustaka):
        self.nama_pustaka = nama_pustaka
        self.daftar_buku = [] 

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
    
    def tampilkan_semua_buku(self):
        print("nama perpustakaan:", self.nama_pustaka)
        print("=" * 45)
        for buku in self.daftar_buku: buku.tampilkan_info()

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                return buku
            return []
        
    def tampilkan_buku_tersedia(self):
        print("Buku yang tersedia di perpustakaan:")
        print("=" * 45)
        for buku in self.daftar_buku:
            if buku.status == "Tersedia":
                buku.tampilkan_info()   

    def tampilkan_buku_dipinjam(self):
        print("Buku yang sedang dipinjam:")
        print("=" * 45)
        for buku in self.daftar_buku:
            if buku.status == "dipinjam":
                buku.tampilkan_info()



