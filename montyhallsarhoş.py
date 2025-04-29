import random
import matplotlib.pyplot as plt

def normal_monty_simulasyon(deneme_sayisi=1000000):
    ilk_kapi_kazanma = 0
    diger_kapi_kazanma = 0
    for i in range(deneme_sayisi):
        araba = random.randint(0, 2)
        secim = random.randint(0, 2)

        if secim == araba:
            kalan_kapilar = [0, 1, 2]
            kalan_kapilar.remove(secim)
            acilan_kapi = random.choice(kalan_kapilar)
        else:
            kalan_kapilar = [0, 1, 2]
            kalan_kapilar.remove(secim)
            kalan_kapilar.remove(araba)
            acilan_kapi = kalan_kapilar[0]

        kalan_kapilar = [0, 1, 2]
        kalan_kapilar.remove(secim)
        kalan_kapilar.remove(acilan_kapi)
        diger_kapi = kalan_kapilar[0]

        if secim == araba:
            ilk_kapi_kazanma += 1

        if diger_kapi == araba:
            diger_kapi_kazanma += 1

    toplam = ilk_kapi_kazanma + diger_kapi_kazanma
    print("Normal Monthy")
    print(f"Toplam oyun: {toplam}")
    print(f"İlk seçilen kapının kazanma oranı: %{ilk_kapi_kazanma / toplam*100:.2f}")
    print(f"Diğer kapının kazanma oranı (değiştirirsen): %{diger_kapi_kazanma / toplam*100:.2f}\n")
    return ilk_kapi_kazanma / toplam * 100, diger_kapi_kazanma / toplam * 100


def sarhos_monty_simulasyon(deneme_sayisi=1000000):
    ilk_kapi_kazanma = 0
    diger_kapi_kazanma = 0
    for i in range(deneme_sayisi):
        araba = random.randint(0, 2)
        secim = random.randint(0, 2)

        kalan_kapilar = [0, 1, 2]
        kalan_kapilar.remove(secim)
        acilan_kapi = random.choice(kalan_kapilar)
        if acilan_kapi == araba:
            continue
        kalan_kapilar.remove(acilan_kapi)
        diger_kapi = kalan_kapilar[0]

        if secim == araba:
            ilk_kapi_kazanma += 1

        if diger_kapi == araba:
            diger_kapi_kazanma += 1

    toplam = ilk_kapi_kazanma + diger_kapi_kazanma
    print("Sarhoş Monthy")
    print(f"Toplam oyun: {toplam}")
    print(f"İlk seçilen kapının kazanma oranı: %{ilk_kapi_kazanma / toplam*100:.2f}")
    print(f"Diğer kapının kazanma oranı (değiştirirsen): %{diger_kapi_kazanma / toplam*100:.2f}\n")
    return ilk_kapi_kazanma / toplam * 100, diger_kapi_kazanma / toplam * 100

def gorsellestir():

    normal_sonuclar = normal_monty_simulasyon()
    sarhos_sonuclar = sarhos_monty_simulasyon()


    etiketler = ['İlk Seçim', 'Değiştirilen Kapı']
    x = range(len(etiketler))

    plt.bar([i - 0.2 for i in x], normal_sonuclar, width=0.4, label='Normal Monty')
    plt.bar([i + 0.2 for i in x], sarhos_sonuclar, width=0.4, label='Sarhoş Monty')

    plt.xlabel('Strateji')
    plt.ylabel('Kazanma Oranı (%)')
    plt.title('Monty Hall Strateji Karşılaştırması')
    plt.xticks(x, etiketler)
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()
if __name__ == "__main__":    
    gorsellestir()