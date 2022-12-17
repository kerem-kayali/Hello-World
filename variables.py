## 7000 TL'lik bir ürün + %18 KDV

"""
print(7000 + (7000 * 0.18))

print(8000 + (8000 * 0.18))
"""

kdv = 0.18
urun1 = 7000
urun2 = 9352

print(urun1 + (urun1 * kdv))
print(urun2 + (urun2 * kdv))

##    DEÐÝÞKEN KULLANIMLARI

# 3urun => yanlýþ. Deðiþkenler sayý ile baþlayamaz.
# urun 4 => yanlýþ. Deðiþkenlerde boþluk kullanýlamaz.
# ürün5 => yanlýþ deðil AMA yine de kullanýlmamalýdýr. (python özelliði sayesinde kullanýlabiliyor)
# urun@ => yanlýþ. Deðiþkenlerde  simge kullanýlamaz.

"""
sayi = 20
SAYI = 30
print(sayi)
print(SAYI)
"""

# Deðiþkenlere sýralý þekilde deðer verilebilir => a, b, c = 10, 3, 35

name = "Kerem" # isimsel veri türü (string)
print(type(name))

isStudent = True # mantýksal veri türü (boolian)
print(type(isStudent))

x = 21 # sayýsal veri türü (intereg)
print(type(x))

y = 2.6 # sayýsal veri türü (float)
print(type(y))

a, b, name, isStudent = 34, 45, "Ahmet", False # bunlarý da sýralý olarak gösterebiliyoruz.
print(type(a, b, name2, isStudent))