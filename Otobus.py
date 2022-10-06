class Otobus:
    """Otobus bilet satis takip sinifi"""
    plaka:str = ""      # otobusun plakasi
    nereden:str = ""    # otobus yolculugunun basladigi durak
    nereye:str = ""     # otobusun yolculugunun bittigi durak
    koltuk_sayisi:int = 0    # otobusteki toplam koltuk sayisi
    dolu_koltuk_saysisi:int = 0     # otobusteki dolu koltuk sayisi
    
    def __init__(self, plaka, nereden, nereye, ksayisi):
        """Constructor
        plaka   otobus plakasi
        nereden     otobus yolculugunun basladigi durak
        nereye      otobusun yolculugunun bittigi durak
        ksayisi     otobusteki toplam koltuk sayisi
        """
        
        self.plaka = plaka
        self.nereden = nereden
        self.nereden = nereye
        self.koltuk_sayisi = ksayisi
    

    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        if self.dolu_koltuk_saysisi < self.koltuk_sayisi:
            self.dolu_koltuk_saysisi = self.dolu_koltuk_saysisi + 1
        
    
    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        if self.dolu_koltuk_saysisi > 0:
            self.dolu_koltuk_saysisi = self.dolu_koltuk_saysisi - 1
        

    
    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        text = "{}, {}, {}, {}, {}"
        print(text.format(self.nereden, self.nereye, self.plaka, self.koltuk_sayisi - self.dolu_koltuk_saysisi, self.dolu_koltuk_saysisi))
        
