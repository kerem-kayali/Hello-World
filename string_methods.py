yazi = "  Merhaba Ben Kerem Kayali. Turkiye'De Yasiyorum.  "

sonuc = yazi.upper() # Metindeki tüm harfleri büyük yapar.
sonuc = yazi.lower() # Metindeki tüm harfleri küçük yapar.
sonuc = yazi.title() # Merindeki tüm kelimelerin baþ harfini büyük yapar.
sonuc = yazi.capitalize() # Sadece cümlenin baþ harfini büyük olarak yazar

print(sonuc)

sonuc = yazi.islower() # Metindeki harflrein hepsi küçük mü diye sorar ve mantýksal cevap verir.
sonuc = yazi.isupper() # Metindeki harflrein hepsi büyük mü diye sorar ve mantýksal   "     " .
sonuc = yazi.istitle() # Metindeki tüm kelimelerin baþ harfi büyük mü diye sorar "    "     " .

print(sonuc)

sonuc = yazi.strip() # Cümledeki boþluklarý yok eder.
sonuc = yazi.split() # CÜmledeki elemanlarý dizi haline getirir.
sonuc = yazi.split(".") # Elemanlarý noktadan itibaren ayýrýr.
sonuc = "-".join(yazi) # Cümledeki her harf arasýna baþa yazdýðýmýz iþareti getirir.

print(sonuc)

sonuc = yazi.index("Kerem") # Metinde bu kelime var mý diye kontrol eder ve kaçýncý indexten itibaren baþladýðýný gösterir.
sonuc = yazi.startswith("m") # Metnin baþladýðý harf "()" içindeki harf mi diye kontrol eder ve mantýksal cevap verir.
sonuc = yazi.endswith(" ") # Metnin bittiði harf "()" içindeki harf mi diye kontrol eder ve mantýksal cevap verir.
sonuc = yazi.replace("Turkiye","Portekiz") # Metinde istediðimiz bir kelimeyi deðiþtirebiliriz.
sonuc = yazi.replace("a","i").replace("t","s").replace("b","u") # Harfleride tek tek böyle deðiþtirebiliriz.

print(sonuc)