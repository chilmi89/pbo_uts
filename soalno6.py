class AlatHidroponikMart:
    def __init__(self, harga, stok):
        self.harga = harga
        self.stok = stok

    def setHarga(self, harga):
        self.harga = harga

    def getHarga(self):
        return self.harga

    def setStok(self, stok):
        self.stok = stok

    def getStok(self):
        return self.stok

    def infoAlatHidroponik(self):
        return f"Harga: {self.harga}, Stok: {self.stok}"

class StarterKitPemula(AlatHidroponikMart):
    def __init__(self, harga, stok, jumlahBaki, holeTutupBaki, warna, namaBenihSayur, jenisNutrisiSayur):
        super().__init__(harga, stok)
        self.jumlahBaki = jumlahBaki
        self.holeTutupBaki = holeTutupBaki
        self.warna = warna
        self.namaBenihSayur = namaBenihSayur
        self.jenisNutrisiSayur = jenisNutrisiSayur

    def setJumlahBaki(self, jumlahBaki):
        self.jumlahBaki = jumlahBaki

    def getJumlahBaki(self):
        return self.jumlahBaki

    def setTutupBaki(self, holeTutupBaki):
        self.holeTutupBaki = holeTutupBaki

    def getTutupBaki(self):
        return self.holeTutupBaki

    def setBenihSayur(self, namaBenihSayur):
        self.namaBenihSayur = namaBenihSayur

    def getBenihSayur(self):
        return self.namaBenihSayur

    def setWarna(self, warna):
        self.warna = warna

    def getWarna(self):
        return self.warna

    def setNutrisiSayur(self, jenisNutrisiSayur):
        self.jenisNutrisiSayur = jenisNutrisiSayur

    def getNutrisiSayur(self):
        return self.jenisNutrisiSayur

    def infoStarterKit(self):
        return f"{self.infoAlatHidroponik()}, Jumlah Baki: {self.jumlahBaki}, Hole Tutup Baki: {self.holeTutupBaki}, Warna: {self.warna}, Nama Benih Sayur: {self.namaBenihSayur}, Jenis Nutrisi Sayur: {self.jenisNutrisiSayur}"

    def infoTotalHargaStarterKit(self):
        harga = self.getHarga()
        if harga >= 450000:
            print("anda mendapatkan diskon sebesar 10%")
            diskon = 0.1 * harga * self.stok
            return harga * self.stok - diskon
        return harga * self.stok

class SetPipa36Hole(AlatHidroponikMart):
    def __init__(self, harga, stok, jumlahPipa, panjangPipa, lebarProduk, tinggiProduk, namaPompa, dayaPompa):
        super().__init__(harga, stok)
        self.jumlahPipa = jumlahPipa
        self.panjangPipa = panjangPipa
        self.lebarProduk = lebarProduk
        self.tinggiProduk = tinggiProduk
        self.namaPompa = namaPompa
        self.dayaPompa = dayaPompa

    def setJumlahPipa(self, jumlahPipa):
        self.jumlahPipa = jumlahPipa

    def getJumlahPipa(self):
        return self.jumlahPipa

    def setPanjangPipa(self, panjangPipa):
        self.panjangPipa = panjangPipa

    def getPanjangPipa(self):
        return self.panjangPipa

    def setLebarProduk(self, lebarProduk):
        self.lebarProduk = lebarProduk

    def getLebarProduk(self):
        return self.lebarProduk

    def setTinggiProduk(self, tinggiProduk):
        self.tinggiProduk = tinggiProduk

    def getTinggiProduk(self):
        return self.tinggiProduk

    def setNamaPompa(self, namaPompa):
        self.namaPompa = namaPompa

    def getNamaPompa(self):
        return self.namaPompa

    def setDayaPompa(self, dayaPompa):
        self.dayaPompa = dayaPompa

    def getDayaPompa(self):
        return self.dayaPompa

    def infoSetPipa(self):
        return f"{self.infoAlatHidroponik()}, Jumlah Pipa: {self.jumlahPipa}, Panjang Pipa: {self.panjangPipa}, Lebar Produk: {self.lebarProduk}, Tinggi Produk: {self.tinggiProduk}, Nama Pompa: {self.namaPompa}, Daya Pompa: {self.dayaPompa}"

    def infoTotalHargaSetPipa(self):
        harga = self.getHarga()
        if harga >= 900000:
            print("anda mendapatkan diskon sebesar 10%")
            diskon = 0.2 * harga * self.getStok()
            return harga * self.getStok() - diskon
        return harga * self.getStok()

data_alat_hidroponik = [
    {
        "nama": "Starter Kit Pemula",
        "harga": 500000,
        "stok": 20,
        "jumlah_baki": 3,
        "hole_tutup_baki": 6,
        "warna": "Merah",
        "nama_benih_sayur": "Kangkung",
        "jenis_nutrisi_sayur": "Urea",
        "kelas": StarterKitPemula
    },
    {
        "nama": "Set Pipa 36 Hole",
        "harga": 1800000,
        "stok": 15,
        "jumlah_pipa": 36,
        "panjang_pipa": 30,
        "lebar_produk": 20,
        "tinggi_produk": 10,
        "nama_pompa": "Pompa air",
        "daya_pompa": 200,
        "kelas": SetPipa36Hole
    }
]

for data in data_alat_hidroponik:
    if data["kelas"] == StarterKitPemula:
        alat_hidroponik = data["kelas"](data["harga"], data["stok"], data["jumlah_baki"], data["hole_tutup_baki"], data["warna"], data["nama_benih_sayur"], data["jenis_nutrisi_sayur"])
        print(alat_hidroponik.infoStarterKit())
        print("Harga Total : Rp. {}".format(alat_hidroponik.infoTotalHargaStarterKit()))
    else:
        alat_hidroponik = data["kelas"](data["harga"], data["stok"], data["jumlah_pipa"], data["panjang_pipa"], data["lebar_produk"], data["tinggi_produk"], data["nama_pompa"], data["daya_pompa"])
        print(alat_hidroponik.infoSetPipa())
        print("Harga Total : Rp. {}".format(alat_hidroponik.infoTotalHargaSetPipa()))

