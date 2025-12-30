class RetailNiaga:
    def __init__(self, nama, punya_kartu_member, total_belanja):
        self.nama = nama
        self.punya_kartu_member = punya_kartu_member
        self.total_belanja_sebelum = total_belanja
        self.__potongan = 0  # private attribute untuk potongan diskon
        self.diskon_persen = 0
        self.diskon_rupiah = 0
        self.total_belanja_setelah = total_belanja
    
    def hitung_diskon(self):
        if self.punya_kartu_member:
            if self.total_belanja_sebelum > 500000:
                self.diskon_persen = 10
            elif 100000 < self.total_belanja_sebelum <= 100000:
                self.diskon_persen = 5
            else:
                self.diskon_persen = 3
        else:
            if self.total_belanja_sebelum > 100000:
                self.diskon_persen = 3
            else:
                self.diskon_persen = 0
        
        self.__potongan = self.diskon_persen / 100
        self.diskon_rupiah = self.total_belanja_sebelum * self.__potongan
        self.total_belanja_setelah = self.total_belanja_sebelum - self.diskon_rupiah
    
    def tampilkan_info(self):
        print(f"Nama Pelanggan       : {self.nama}")
        print(f"Status Kartu Member  : {'Ya' if self.punya_kartu_member else 'Tidak'}")
        print(f"Total Belanja Sebelum: Rp {self.total_belanja_sebelum:,}")
        print(f"Diskon               : {self.diskon_persen}%")
        print(f"Diskon (dalam rupiah): Rp {int(self.diskon_rupiah):,}")
        print(f"Total Belanja Setelah: Rp {int(self.total_belanja_setelah):,}")

# Contoh penggunaan program
pelanggan1 = RetailNiaga("RIO", True, 600000)
pelanggan1.hitung_diskon()
pelanggan1.tampilkan_info()

print("\n")

pelanggan2 = RetailNiaga("TIO", False, 150000)
pelanggan2.hitung_diskon()
pelanggan2.tampilkan_info()

print("\n")

pelanggan3 = RetailNiaga("RIVAL", True, 90000)
pelanggan3.hitung_diskon()
pelanggan3.tampilkan_info()