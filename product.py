class Produk():
    jumlah_produk = 0
    
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        Produk.jumlah_produk += 1
        
    def berapa_jumlah():
        print('Total Produk Kita: ', Produk.jumlah_produk)
        
    def detail_produk(self):
        print("Nama : ", self.nama)
        print("Harga: ", self.harga)
        print()
        
# membuat objek pertama
produk1 = Produk('ES KELAPA', 15000)

# membuat objek kedua
produk2 = Produk('ES DOGER', 10000)

# mengakses attribut objek
produk1.detail_produk()
produk2.detail_produk()
Produk.berapa_jumlah()
