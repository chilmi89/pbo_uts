class TokoElektronik:
    def __init__(self, harga, warna, stok):
        self.__harga = harga
        self.warna = warna
        self.stok = stok

    def get_harga(self):
        return self.__harga

    def set_harga(self, harga):
        self.__harga = harga

    def get_warna(self):
        return self.warna

    def set_warna(self, warna):
        self.warna = warna

    def get_stok(self):
        return self.stok

    def set_stok(self, stok):
        self.stok = stok

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
        return self.get_harga() * self.stok
    
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
        if harga >= 2320000:
            print("anda mendapatkan diskon sebesaer 10 %")
            diskon = 0.1 * harga * self.stok
            return harga * self.stok - diskon
    
Z


