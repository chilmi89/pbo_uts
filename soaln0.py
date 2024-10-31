class TokoElektronik:
    def __init__(self, harga, warna, stok):
        self.harga = harga
        self.warna = warna
        self.stok = stok

    def get_harga(self):
        return self.harga

    def set_harga(self, harga):
        self.harga = harga

    def get_warna(self):
        return self.warna

    def set_warna(self, warna):
        self.warna = warna

    def get_stok(self):
        return self.stok

    def set_stok(self, stok):
        self.stok = stok


class Televisi(TokoElektronik):
    def __init__(self, harga, warna, stok, ukuran, resolusi, konektivitas, konsumsiDaya, berat):
        super().__init__(harga, warna, stok)
        self.ukuran = ukuran
        self.resolusi = resolusi
        self.konektivitas = konektivitas
        self.konsumsiDaya = konsumsiDaya
        self.berat = berat

    def setUkuran(self, ukuran):
        self.ukuran = ukuran

    def getUkuran(self):
        return self.ukuran


    def setResolusi(self, resolusi):
        self.resolusi = resolusi

    def getResolusi(self):
        return self.resolusi

    def setKonektivitas(self, konektivitas):
        self.konektivitas = konektivitas

    def getKonektivitas(self):
        return self.konektivitas

    def setKonsumsiDaya(self, konsumsiDaya):
        self.konsumsiDaya = konsumsiDaya

    def getKonsumsiDaya(self):
        return self.konsumsiDaya

    def setBerat(self, berat):
        self.berat = berat

    def getBerat(self):
        return self.berat

    def infoTV(self):
        return "Warna : {} , Ukuran : {} , Resolusi : {} , Konektivitas : {} , Konsumsi Daya : {} , Berat : {} , Harga : {}".format(self.warna, self.ukuran, self.resolusi, self.konektivitas, self.konsumsiDaya, self.berat, self.harga)

    def hargaTotalTV(self):
        harga = self.harga 
        if harga >= 2500000 or self.stok == 2:
            print("anda mendapatkan diskon sebesaer 15 %")
            diskon = 0.15 * harga * self.stok
            return harga - diskon
        else:
            return "maaf anda tidak mendapat diskon", harga



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
        return "Warna : {} , Kapasitas : {} , Tipe : {} , Harga : {}".format(self.warna, self.kapasitas, self.type, self.harga)

    def hargaTotalMesinCuci(self):
        return self.harga * self.stok



tv1 = Televisi(120000, "silver", 8, "42 inch", "Full HD", "HDMI, USB", 120, 7)
tv2 = Televisi(1500000, "black", 5, "55 inch", "4K", "HDMI, USB, Wi-Fi", 150, 10)
data_tv = [tv1, tv2]

mc = Mesin_cuci(2000000, "putih", 5, "8kg", "Front Load")
mc2 = Mesin_cuci(2000000, "hitam", 5, "8kg", "back Load")





