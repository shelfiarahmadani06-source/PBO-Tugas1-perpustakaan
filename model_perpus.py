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
        
class anggota:
    def __init__(self, nama, NIM, semester):
        self.nama = nama
        self.NIM = NIM
        self.semester = semester
        self.buku_dipinjam = None

    def pinjam_buku(self, buku):
        if buku.status == "Tersedia" and buku.stok > 0: 
            buku.status = "dipinjam"
            buku.stok -= 1 
            self.buku_dipinjam = buku
            print(f"{self.nama} berhasil meminjam buku {buku.judul}")
        else: 
            print(f"maaf, buku {buku.judul} sedang tidak tersedia untuk dipinjam saat ini. datang kembali nanti😊")
    
    def kembalikan_buku(self):
        if self.buku_dipinjam:
            self.buku_dipinjam.status = "tersedia"
            self.buku_dipinjam.stok += 1
            print(f"{self.nama} berhasil mengembalikan buku {self.buku_dipinjam.judul}")
            self.buku_dipinjam = None
        else:
            print("anda tidak meminjam buku apapun.")

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



