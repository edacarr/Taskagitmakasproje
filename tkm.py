import random

def tas_kagit_makas_eda_acar():

    print("Merhaba! Taş, Kağıt, Makas, Ateş oyununa hoş geldiniz!")
    print("Oyunun kuralları:")
    print("1. Taş, Kağıt, Makas veya Ateş arasından bir seçim yapılır.")
    print("2. İlk iki turu kazanan oyunu kazanır.")
    print("3. Kazanma kuralları:")
    print(".Taş; Makas ve Ateş'i yener, Kağıt'a yenilir.")
    print(".Kağıt; Taş ve Ateş'i yener, Makas'a yenilir.")
    print(".Makas; Kağıt'ı yener, Taş ve Ateş'e yenilir.")
    print(".Ateş; Kağıt ve Makas'ı yener, Taş'a yenilir.")
    print("İyi şanslar :) \n")

    options = ["taş", "kağıt", "makas", "ateş"]

    oynanan_oyun = 0

    while True:
        oyuncu_galibiyet = 0
        bilgisayar_galibiyet = 0
        oynanan_oyun += 1
        print(f"Oyun {oynanan_oyun} başlıyor!")

        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            oyuncu_secim = input("Taş, Kağıt, Makas, Ateş? ").lower()

            if oyuncu_secim not in options:
                print("Geçersiz bir seçenek girdiniz. Lütfen 'taş', 'kağıt', 'makas' veya 'ateş' seçin.")
                continue

            bilgisayar_secim = random.choice(options)
            print(f"Bilgisayarın seçimi: {bilgisayar_secim}")

            # Kazananı belirleme
            if oyuncu_secim == bilgisayar_secim:
                print("Beraberlik sağlandı!")
            elif (oyuncu_secim == "taş" and bilgisayar_secim in ["makas", "ateş"]) or \
                 (oyuncu_secim == "kağıt" and bilgisayar_secim in ["taş", "ateş"]) or \
                 (oyuncu_secim == "makas" and bilgisayar_secim in ["kağıt"]) or \
                 (oyuncu_secim == "ateş" and bilgisayar_secim in ["kağıt", "makas"]):
                print("Tebrikler bu turu siz kazandınız!")
                oyuncu_galibiyet += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_galibiyet += 1

            print(f"Skor: Oyuncu {oyuncu_galibiyet} - {bilgisayar_galibiyet} Bilgisayar\n")

        if oyuncu_galibiyet == 2:
            print("Tebrikler, oyunu kazandınız!")
        else:
            print("Bilgisayar oyunu kazandı!")

        devam = input("Başka bir oyun oynamak ister misiniz? (e/h): ").lower()
        bilgisayar_devam = random.choice(["e", "h"])
        print(f"Bilgisayarın devam kararı şu şekildedir: {'Evet' if bilgisayar_devam == 'e' else 'Hayır'}")

        if devam != 'e' or bilgisayar_devam != 'e':
            print("Oyun sona erdi. Oynadığınız için teşekkürler :)")
            break
        else:
            print("Yeni bir oyun başlıyor...\n")

tas_kagit_makas_eda_acar()
