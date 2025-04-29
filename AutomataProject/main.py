import os
from graphviz import Digraph

# DFA (Deterministic Finite Automata) sınıfı
class DFA:
    def __init__(self, durumlar, alfabe, gecisler, baslangic_durumu, kabul_durumlari):
        self.durumlar = durumlar
        self.alfabe = alfabe
        self.gecisler = gecisler
        self.baslangic_durumu = baslangic_durumu
        self.kabul_durumlari = kabul_durumlari

    # Girdi doğrulama fonksiyonu
    def girdi_dogrula(self, girdi_dizisi):
        mevcut_durum = self.baslangic_durumu
        print(f"Başlangıç durumu: {mevcut_durum}")

        # Girdi dizisindeki her sembolü kontrol et
        for sembol in girdi_dizisi:
            if sembol not in self.alfabe:
                # Eğer sembol alfabede tanımlı değilse hata ver
                print(f"Hata: '{sembol}' alfabede tanımlı değil!")
                return False
            
            # Geçiş tablosundan mevcut durumu kontrol et
            if mevcut_durum in self.gecisler and sembol in self.gecisler[mevcut_durum]:
                # Geçerli bir geçiş varsa, yeni duruma geç
                mevcut_durum = self.gecisler[mevcut_durum][sembol]
                print(f"Yeni durum: {mevcut_durum}")
            else:
                # Eğer geçiş bulunamazsa hata mesajı göster
                print(f"Hata: '{mevcut_durum}' durumunda '{sembol}' için geçiş bulunamadı!")
                return False
        
        # Son durum kabul durumlarından biriyse kabul et
        if mevcut_durum in self.kabul_durumlari:
            print("Girdi kabul edildi.")
            return True
        else:
            print("Girdi reddedildi.")
            return False

    # DFA'yı görselleştirme fonksiyonu
    def gorsellestir(self, dosya_adi="dfa"):
        grafik = Digraph(format="png")
        
        # Durumları ekle ve kabul durumlarını işaretle
        for durum in self.durumlar:
            sekil = "doublecircle" if durum in self.kabul_durumlari else "circle"
            grafik.node(durum, shape=sekil)
        
        # Başlangıç durumu işaretle
        grafik.node("", shape="none")
        grafik.edge("", self.baslangic_durumu)
        
        # Geçişleri çiz
        for mevcut_durum, semboller in self.gecisler.items():
            for sembol, yeni_durum in semboller.items():
                grafik.edge(mevcut_durum, yeni_durum, label=sembol)
        
        # Görselleştirme dosyasını oluştur
        try:
            grafik.render(dosya_adi, view=True)
            print(f"Görselleştirme oluşturuldu: {dosya_adi}.png")
        except Exception as e:
            print(f"Görselleştirme sırasında hata oluştu: {e}")

# Ekranı temizleme fonksiyonu
def ekran_temizle():
    os.system("cls")

# Kullanıcıdan DFA bilgilerini alma fonksiyonu
def kullanicidan_dfa_al():
    print("DFA tanımlama")
    durumlar = input("Durumlar (virgülle ayrılmış): ").strip().split(",")
    alfabe = input("Alfabe sembolleri (virgülle ayrılmış): ").strip().split(",")
    baslangic_durumu = input("Başlangıç durumu: ").strip()
    kabul_durumlari = input("Kabul durumları (virgülle ayrılmış): ").strip().split(",")

    gecisler = {}
    print("Geçişleri tanımlayın [format: (mevcut_durum) (sembol) (yeni_durum)]. 'bitti' yazarak çıkabilirsiniz.")
    while True:
        gecis = input("Geçiş: ").strip()
        if gecis == "bitti":
            break
        try:
            mevcut_durum, sembol, yeni_durum = gecis.split()
            if mevcut_durum not in durumlar or yeni_durum not in durumlar:
                print("Hata: Durumlar geçerli değil!")
                continue
            if sembol not in alfabe:
                print("Hata: Sembol alfabede tanımlı değil!")
                continue
            if sembol in gecisler.get(mevcut_durum, {}):
                print(f"Hata: '{mevcut_durum}' durumunda '{sembol}' için zaten bir geçiş tanımlı!")
                continue
            gecisler.setdefault(mevcut_durum, {})[sembol] = yeni_durum
        except ValueError:
            print("Hatalı giriş! Format: mevcut_durum sembol yeni_durum")

    # Eksik geçişleri tamamlamak için kullanıcıdan bilgi alma
    while True:
        eksik_gecis_var = False
        for durum in durumlar:
            for sembol in alfabe:
                if sembol not in gecisler.get(durum, {}):
                    eksik_gecis_var = True
                    print(f"'{durum}' durumu için '{sembol}' sembolüyle geçiş tanımlanmamış!")
                    try:
                        yeni_durum = input(f"Geçişi tamamlayın: {durum} {sembol} -> ").strip()
                        if yeni_durum not in durumlar:
                            print("Hata: Geçerli bir durum giriniz!")
                            continue
                        gecisler.setdefault(durum, {})[sembol] = yeni_durum
                    except ValueError:
                        print("Hatalı giriş!")
        if not eksik_gecis_var:
            break

    return DFA(durumlar, alfabe, gecisler, baslangic_durumu, kabul_durumlari)


dfa = kullanicidan_dfa_al()

while True:
    ekran_temizle()
    print("\nSeçenekler:")
    print("1 - Girdi kontrol et")
    print("2 - DFA'yı görselleştir")
    print("3 - Çıkış")
    secim = input("Seçiminiz: ").strip()
    ekran_temizle()

    if secim == "1":
        girdi_dizisi = input("Girdi dizisini girin: ").strip()
        dfa.girdi_dogrula(girdi_dizisi)
        input("\nDevam etmek için Enter'a basın...")
    elif secim == "2":
        dosya_adi = input("Dosya adı (varsayılan 'dfa'): ").strip() or "dfa"
        dfa.gorsellestir(dosya_adi)
        input("\nDevam etmek için Enter'a basın...")
    elif secim == "3":
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")
