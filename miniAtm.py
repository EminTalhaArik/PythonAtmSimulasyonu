# -*- coding: utf-8 -*-

userName = "admin"

password = "1234"

bakiye = 0

def paraYatir(bakiye):s
    
    yatirilacakTutar = int(input("Lütfen Yatırmak İstediğiniz Tutarı Giriniz : "))
    
    guncelBakiye = bakiye + yatirilacakTutar

    return guncelBakiye
    
def paraCek(bakiye, cekilecekTutar):
        
    guncelBakiye = bakiye - cekilecekTutar
    
    return guncelBakiye

def bakiyeGoruntule(bakiye):
    
    print("Güncel Bakiyeniz = " + str(bakiye))


devam  = True

print("--------------------- ATM Simulasyonuna Hoşgeldiniz ---------------------")

girisKullaniciAdi = input("Lütfen Bir Kullanıcı Adı Giriniz : ")

if girisKullaniciAdi == userName:
    girisSifre = input("Lütfen Şifrenizi Giriniz : ")
    
    if girisSifre == password:
        
        while devam:
            
            print("1 - Para Yatır , 2 - Para Çek , 3 - Bakiye Görüntüle , 0 - Çıkış Yap")
        
            try:
                secim = int(input("Lütfen Bİr İşlem Giriniz : "))
            except ValueError:
                print("Lütfen Sayı Giriniz.")
                
            print("------------İşlem Yapılıyor---------------")
            
            
            if secim == 1:
                bakiye = paraYatir(bakiye)
                print("=========================")
                print("Para yatırma İşleminiz Onaylanmıştır.")
                print("=========================")
            elif secim == 2:
                
                cekilecekTutar = int(input("Lütfen Para Çekiceğiniz Tutarı Giriniz : "))
                
                if paraCek(bakiye, cekilecekTutar) < 0:
                    print("=========================")
                    print("Bakiyeniz Yeterli Değildir.")
                    print("=========================")
                else:
                    bakiye = paraCek(bakiye, cekilecekTutar)
                    print("=========================")
                    print("Para Çekme İşleminiz Onaylanmıştır.")
                    print("=========================")
                    
            elif secim == 3:
                bakiyeGoruntule(bakiye)
                
            elif secim == 0:
                devam = False
                print("=========================")
                print("Çıkış Yapıldı.")
                print("=========================")
    
    else:
        print("Hatalı Parola")
        
else:
    print("Hatalı Giriş")

