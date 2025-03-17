import pandas as pd
import math

input_filename = "denklemler-221401002.csv"
output_filename = "kökler-221401002.csv"

df = pd.read_csv(input_filename)


def root_Finder(row):
    a = row["a"]
    b = row["b"]
    c = row["c"]

    # Diskriminantı hesapla
    Diskriminant = b ** 2 - 4 * a * c

    if Diskriminant < 0:
        # Reel kök olmama durumu:
        return pd.Series({"x1": "-", "x2": "-", "sınıf": "Reel kök yoktur"})
    elif Diskriminant == 0:
        # Çift katlı tek kök olma durumu:
        root = -b / (2 * a)
        return pd.Series({"x1": f"{root:.4f}", "x2": f"{root:.4f}", "sınıf": "Tek kök vardır"})
    else:
        # Birbirinden farklı iki reel kök olma durumu:
        karekökDisk = math.sqrt(Diskriminant)
        root1 = (-b - karekökDisk) / (2 * a)
        root2 = (-b + karekökDisk) / (2 * a)

        # x1 küçük olan x2 büyük olan olsun:
        x1 = f"{min(root1, root2):.4f}"
        x2 = f"{max(root1, root2):.4f}"
        return pd.Series({"x1": x1, "x2": x2, "sınıf": "İki reel kök vardır"})


# Her satır için hesaplamaları uygula
kokler_df = df.apply(root_Finder, axis=1)

# Sonuçları orijinal DataFrame ile birleştir
sonuc_df = pd.concat([df, kokler_df], axis=1)

# Çıktıyı istenen formatta CSV dosyasına yaz (sütun sırası: a, b, c, x1, x2, sınıf)
sonuc_df.to_csv(output_filename, index=False)
