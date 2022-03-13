from abc import abstractmethod, ABC

# ya 
def hallo():
    print("Halloo")
    
    

class Binatang(ABC):
    
    #Abstract Method
    @abstractmethod
    def Peternakan(self):
        pass
    
    
class Sapi(object):  
    nama_Sapi = ""
    def __init__(self, input_nama, input_usia, input_warna, input_jenis):
        self.nama = input_nama
        self.usia = input_usia
        self.warna = input_warna
        self.jenis = input_jenis
        Sapi.nama_Sapi = input_nama

    def mooo(self):
        print("mmoooo... ", self.nama)

    def info(self):
        print(f"nama: {self.nama}, usia: {self.usia}, warna: {self.warna}, jenis: {self.jenis}")

        
class Binatang(object):
    def __init__(self, nama, usia, jenis, mamalia):
        self.nama = nama
        self.usia = usia
        self.jenis = jenis
        self.mamalia = mamalia

    def __tidur(self, durasi):
        for x in range(durasi):
            print("ddrrr... ddrrr... ")

    def info(self):
        self.__tidur(2)
        print(f"nama: {self.nama}, usia: {self.usia}, jenis: {self.jenis}, mamalia: {self.mamalia}")
        

class Sapi(Binatang):
    def __init__(self,  nama, usia, jenis, mamalia, warna, jenis_Sapi):
        super().__init__(nama, usia, jenis, mamalia)
        self.warna = warna
        self.jenis_Sapi = jenis_Sapi

    def mooo(self):
        super()._tidur(2)
        print("mmoooo")

    def info_Sapi(self):
        super().info()
        print(f"warna: {self.warna}, jenis Sapi: {self.jenis_Sapi}")        
        
        
class Kendaraan(ABC):
    
    @abstractmethod
    def suara(self):
        pass
    
class Pesawat(Kendaraan):
    def suara(self):
        print("wessstt")
        

class Bus(Kendaraan):
    def suara(self):
        print("mbemmm")
       
        
class Kereta(Kendaraan):
    def suara(self):
        print("juggjugg")
        
        
class Binatang(object):
    
    def __init__(self, nama, usia, jenis, mamalia):
        self.nama = nama
        self.usia = usia
        self.jenis = jenis
        self.mamalia = mamalia

    def tidur(self, durasi):
        for x in range(durasi):
            print("dddrrrr.... dddrrrr.... ")

    def info(self):
        print(f"nama: {self.nama}, usia: {self.usia}, jenis: {self.jenis}, mamalia: {self.mamalia}")


class Ular(Binatang):
    def __init__(self,  nama, usia, jenis, mamalia, warna, jenis_habitat, jenis_ular):
        super().__init__(nama, usia, jenis, mamalia)
        self.warna = warna
        self.jenis_habitat = jenis_habitat
        self.jenis_ular = jenis_ular
  
    def melata(self, durasi):
        print("ssttt... ssttt... ")

    def info_Ular(self):
        print(f"warna: {self.warna}, jenis ular: {self.jenis_ular}, jenis habitat: {self.jenis_habitat}")

class Monyet(Binatang):
    def __init__(self, nama, usia, jenis, mamalia, warna):
        super().__init__(nama, usia, jenis, mamalia)
        self.warna = warna
    
    def info_Monyet(self):
        print(f"warna: {self.warna}")
  
    def makan_pisang(self, buah):
        if buah >=7 :
            print("kenyaang")
        else:
            print("lapaar")
    