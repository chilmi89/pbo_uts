class TokoElektronik:
    def __init__(self, harga, warna, stok):
        self.harga = harga
        self.warna = warna
        self.stok = stok

    def setHarga(self, harga):
        self.harga = harga

    def getHarga(self):
        return self.harga

    def setWarna(self, warna):
        self.warna = warna

    def getWarna(self):
        return self.warna

    def infoToko(self):
        return f"Harga: {self.harga}, Warna: {self.warna}, Stok: {self.stok}"
    
class Mesin_cuci(TokoElektronik):
    def __init__(self, harga, warna, stok, kapasitas, type):
        super().__init__(harga, warna, stok)
        self.kapasitas = kapasitas
        self.type = type

    def setKapasitas(self, kapasitas):
        self.kapasitas = kapasitas

    def getKapasitas(self):
        return self.kapasitas

    def setTipe(self, tipe):
        self.type = tipe

    def getTipe(self):
        return self.type

    def infoMesinCuci(self):
        return "Warna : {} , Kapasitas : {} , Tipe : {} ".format(self.warna, self.kapasitas, self.type)

    def hargaTotalMesinCuci(self):
        return self.harga * self.stok


class Kulkas (TokoElektronik):
    def __init__(self, harga, warna, stok, model, KapasitasFreezer, teknologiPendingin, konsumsiDaya, berat):
        super().__init__(harga, warna, stok)
        self.model = model
        self.KapasitasFreezer = KapasitasFreezer
        self.teknologiPendingin = teknologiPendingin
        self.konsumsiDaya = konsumsiDaya
        self.berat = berat

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model

    def setKapasitasFreezer(self, KapasitasFreezer):
        self.KapasitasFreezer = KapasitasFreezer

    def getKapasitasFreezer(self):
        return self.KapasitasFreezer

    def setteknologiPendingin(self, teknologiPendingin):
        self.teknologiPendingin = teknologiPendingin

    def getteknologiPendingin(self):
        return self.teknologiPendingin

    def setKonsumsiDaya(self, konsumsiDaya):
        self.konsumsiDaya = konsumsiDaya

    def getKonsumsiDaya(self):
        return self.konsumsiDaya

    def setBerat(self, berat):
        self.berat = berat

    def getBerat(self):
        return self.berat

    def infoKulkas(self):
        return "Warna : {} , Model : {} , KapasitasFreezer : {} , teknologiPendingin : {} , Konsumsi Daya : {} , Berat : {} ".format(self.warna, self.model, self.KapasitasFreezer, self.teknologiPendingin, self.konsumsiDaya, self.berat)

    def hargaTotalKulkas(self):
        harga = self.get_harga()
        if harga >= 3120000:
            print("anda mendapatkan diskon sebesaer 10 %")
            diskon = 0.2 * harga * self.stok
            return harga * self.stok - diskon



mesin_cuci1 = Mesin_cuci(1500000, "Putih", 5, 8, "Bukaan Depan")
mesin_cuci2 = Mesin_cuci(2000000, "Hitam", 3, 10, "Bukaan Atas")
print(mesin_cuci1.infoMesinCuci())
print(mesin_cuci2.infoMesinCuci())

kulkas1 = Kulkas(2500000, "Hitam", 3, "Side by Side", 100, "No Frost", 250, 70)
kulkas2 = Kulkas(1800000, "Silver", 2, "Two Door", 80, "Direct Cool", 200, 60)
# print("Type Mesin Cuci:")
# print(type(mesin_cuci1))
# print(type(mesin_cuci2))

print(kulkas1.infoKulkas())
print(kulkas2.infoKulkas())


# HARGA YANG MENDAPATKAN DISKON
print(kulkas1.hargaTotalKulkas())

# HARGA YANG TIDAK MENDAPATKAN DISKON
print(kulkas2.hargaTotalKulkas())


