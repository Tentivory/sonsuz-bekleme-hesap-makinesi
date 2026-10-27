#!/usr/bin/env python3
# Dünyanın En Yavaş Hesap Makinesi
# Her işlem en az 5 saniye sürer. Felsefe bedava.

import time
import random
import sys

# Gizli değişken (hiç kullanılmaz, sadece saklıdır)
_gizli_mesaj = "ZGVtb2tyYXNpIGhlcmtlc2UgbGF6xLFtLiBBbWEga2ltc2UgYmVrbGVtaXlvci4="  # base64, decode etmeyin yoksa siyaset olur

def felsefi_gecikme():
    bekleme = random.randint(3, 10)
    felsefeler = [
        "Hayat da böyle, bazen beklemek gerekir...",
        "Sonsuzluk bir anda mı başlar yoksa bekleyince mi?",
        "Matematik bile acele etmez, sen neden ediyorsun?",
        "Çay demlenirken hesap yapmak günahtır.",
        "Beklemek bir erdemdir, özellikle hesap makinesinde."
    ]
    print(f"\n{random.choice(felsefeler)}")
    print(f"Bekleniyor... {bekleme} saniye (bu süreçte evren genişliyor)")
    time.sleep(bekleme)

def topla(a, b):
    felsefi_gecikme()
    sonuc = a + b
    print(f"Sonuç: {sonuc} (ama asıl sonuç sabırdır)")
    return sonuc

def cikar(a, b):
    felsefi_gecikme()
    sonuc = a - b
    print(f"Sonuç: {sonuc} (eksi de olsa hayat devam eder)")
    return sonuc

def carp(a, b):
    felsefi_gecikme()
    sonuc = a * b
    print(f"Sonuç: {sonuc} (çoğaltmak kolay, anlamak zor)")
    return sonuc

def bol(a, b):
    if b == 0:
        felsefi_gecikme()
        print("Sıfıra bölme yasaktır. Evren çökerdi yoksa. Sonuç: sonsuz (veya hata)")
        return float('inf')
    felsefi_gecikme()
    sonuc = a / b
    print(f"Sonuç: {sonuc} (paylaşmak güzeldir)")
    return sonuc

def main():
    print("="*50)
    print("DÜNYANIN EN YAVAŞ HESAP MAKİNESİ")
    print("Versiyon: 1.0 - Sonsuzluk Edition")
    print("Uyarı: Bu program hızlı çalışmaz. Hiçbir şey hızlı çalışmaz.")
    print("="*50)
    
    while True:
        print("\nİşlemler: + - * /  veya 'q' çıkış")
        islem = input("İşlem seç: ").strip()
        
        if islem.lower() == 'q':
            print("Çıkış yapılıyor... Bu da 5 saniye sürebilir.")
            time.sleep(5)
            print("Güle güle. Bir daha gelme, çok yavaşsın.")
            break
        
        try:
            a = float(input("Birinci sayı: "))
            b = float(input("İkinci sayı: "))
        except ValueError:
            print("Sayı gir kardeşim, felsefe yetmez.")
            continue
        
        if islem == '+':
            topla(a, b)
        elif islem == '-':
            cikar(a, b)
        elif islem == '*':
            carp(a, b)
        elif islem == '/':
            bol(a, b)
        else:
            print("Geçersiz işlem. Evren bunu kabul etmiyor.")
            time.sleep(2)

if __name__ == "__main__":
    main()
