## 7000 TL'lik bir �r�n + %18 KDV

"""
print(7000 + (7000 * 0.18))

print(8000 + (8000 * 0.18))
"""

kdv = 0.18
urun1 = 7000
urun2 = 9352

print(urun1 + (urun1 * kdv))
print(urun2 + (urun2 * kdv))

##    DE���KEN KULLANIMLARI

# 3urun => yanl��. De�i�kenler say� ile ba�layamaz.
# urun 4 => yanl��. De�i�kenlerde bo�luk kullan�lamaz.
# �r�n5 => yanl�� de�il AMA yine de kullan�lmamal�d�r. (python �zelli�i sayesinde kullan�labiliyor)
# urun@ => yanl��. De�i�kenlerde  simge kullan�lamaz.

"""
sayi = 20
SAYI = 30
print(sayi)
print(SAYI)
"""

# De�i�kenlere s�ral� �ekilde de�er verilebilir => a, b, c = 10, 3, 35

name = "Kerem" # isimsel veri t�r� (string)
print(type(name))

isStudent = True # mant�ksal veri t�r� (boolian)
print(type(isStudent))

x = 21 # say�sal veri t�r� (intereg)
print(type(x))

y = 2.6 # say�sal veri t�r� (float)
print(type(y))

a, b, name, isStudent = 34, 45, "Ahmet", False # bunlar� da s�ral� olarak g�sterebiliyoruz.
print(type(a, b, name2, isStudent))