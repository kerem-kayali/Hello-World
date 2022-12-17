name = "Kerem"
surname = "Kayali"
age = 14

text = "Benim adim " + name + " " + surname + "."
print(text)

print(text[0]) # "B"
print(text[1]) # "e"
print(text[-1]) # "."

print(text[0:5]) # "Benim"
print(text[0:24]) # "Benim adim Kerem Kayali."
print(text[:10]) # "Benim adim"
print(text[0:]) # Tüm metni belirtir.

print(text[-13:-1]) # "Kerem Kayali"
print(text[0:24:2]) # "Bnmai ee aai"

print(text[:]) # Tüm metni belirtir.
print(text[::2])  # En sondaki sayý kadar atlaya atlaya en sona kadar metni belirtir.
print(text[::-2]) # "     "      "    "     "      "    "    "    "     "   ters taraftan belirtir.
print(text[::-1]) # Tüm metni ters þekilde belirtir.