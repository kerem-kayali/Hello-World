name = "Kerem"
surname = "Kayali"
age = "14"

print("My name is {} {} and im {} years old".format(name,surname,age))

# Format komutu süslü parantezin içine istediðimiz komutu göndermemizi saðlar.
# Yani "string_slicing.py" dosyasýnda yaptýðýmýz gibi uzun uzun yazmamýza gerek kalmaz.

print("My name is {1} {0}".format(name,surname)) # Süslü parantezin içine numara yazarak indexi belirleyebiliyoruz.

print("My name is {s} {n}".format(n=name,s=surname)) # Isimlere takma ad verip yine sýralarýný belirleyebiliyoruz.
print("My name is {n} {s}".format(n=name,s=surname))

print("My name is {0} {1} and im {2} years old. {2}".format(name,surname,age))

number = 5 / 3
print("The result is {n:1.3}".format(n=number))

print(f"My name is {name} {surname} and I'm {age} years old.") # pythonun bir özelliði sayesinde formatlarý böyle de kullanabiliyoruz.