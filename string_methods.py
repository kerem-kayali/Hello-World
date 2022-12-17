yazi = "  Merhaba Ben Kerem Kayali. Turkiye'De Yasiyorum.  "

sonuc = yazi.upper() # Metindeki t�m harfleri b�y�k yapar.
sonuc = yazi.lower() # Metindeki t�m harfleri k���k yapar.
sonuc = yazi.title() # Merindeki t�m kelimelerin ba� harfini b�y�k yapar.
sonuc = yazi.capitalize() # Sadece c�mlenin ba� harfini b�y�k olarak yazar

print(sonuc)

sonuc = yazi.islower() # Metindeki harflrein hepsi k���k m� diye sorar ve mant�ksal cevap verir.
sonuc = yazi.isupper() # Metindeki harflrein hepsi b�y�k m� diye sorar ve mant�ksal   "     " .
sonuc = yazi.istitle() # Metindeki t�m kelimelerin ba� harfi b�y�k m� diye sorar "    "     " .

print(sonuc)

sonuc = yazi.strip() # C�mledeki bo�luklar� yok eder.
sonuc = yazi.split() # C�mledeki elemanlar� dizi haline getirir.
sonuc = yazi.split(".") # Elemanlar� noktadan itibaren ay�r�r.
sonuc = "-".join(yazi) # C�mledeki her harf aras�na ba�a yazd���m�z i�areti getirir.

print(sonuc)

sonuc = yazi.index("Kerem") # Metinde bu kelime var m� diye kontrol eder ve ka��nc� indexten itibaren ba�lad���n� g�sterir.
sonuc = yazi.startswith("m") # Metnin ba�lad��� harf "()" i�indeki harf mi diye kontrol eder ve mant�ksal cevap verir.
sonuc = yazi.endswith(" ") # Metnin bitti�i harf "()" i�indeki harf mi diye kontrol eder ve mant�ksal cevap verir.
sonuc = yazi.replace("Turkiye","Portekiz") # Metinde istedi�imiz bir kelimeyi de�i�tirebiliriz.
sonuc = yazi.replace("a","i").replace("t","s").replace("b","u") # Harfleride tek tek b�yle de�i�tirebiliriz.

print(sonuc)