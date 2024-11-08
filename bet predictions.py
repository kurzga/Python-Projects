def minimize_kayip(bahis_oranlari, para_miktari):
    toplam_oran = sum(bahis_oranlari)
    bahis_miktarlari = []

    for oran in bahis_oranlari:
        bahis_miktar = (para_miktari * oran) / toplam_oran
        bahis_miktarlari.append(bahis_miktar)

    return bahis_miktarlari

# Örnek kullanım:
bahis_oranlari = [1.98,3.46,2.53]  # Örnek bahis oranları
para_miktari = 100 # Örnek para miktarı

bahis_miktarlari = minimize_kayip(bahis_oranlari, para_miktari)
for i, bahis_miktar in enumerate(bahis_miktarlari):
    print(f"Oran {i+1}: {bahis_miktar:.2f} birim")
